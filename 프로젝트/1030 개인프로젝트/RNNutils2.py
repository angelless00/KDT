import re
from collections import Counter
import numpy as np
import torch
import os
device = "cuda" if torch.cuda.is_available() else 'cpu'


def getToken(textlist,tokenizer):
    text_to_token=[]
    for idx,text in enumerate(textlist):
        # 한글빼고 다지우기
        #text=re.sub('[^ㄱ-ㅎ가-힣]+',' ',text)

        # 토큰 내놔 norm,stem << 참고
        tokens=tokenizer.morphs(text)
        text_to_token.append(tokens)

    return text_to_token


def get_vocab(text_to_token,n_vocab):
    """단어사전 생성 n_vocab 갯수만큼"""
    tokenlist=[token for token in text_to_token]
    counter=Counter()
    for tokens in tokenlist:
        
            counter.update(tokens)
    vocab=['<pad>','<oov>']
    for token,count in counter.most_common(n_vocab):
        vocab.append(token)
    return vocab

def vectorize(tokenlist,token_to_idx):
    idxlist=[]
    for tokens in tokenlist:
        numbers=[token_to_idx.get(token) for token in tokens]
        idxlist.append(numbers)
    return idxlist


def padding_vectorize(tokenlist,token_to_idx,pad_length):
    """pad 길이맞추고, 수치화"""
    idxlist=[]
    oov_num=token_to_idx['<oov>']
    for tokens in tokenlist:
        if len(tokens)>=pad_length:
            tokens=tokens[:pad_length]
        else:
            tokens=tokens+(['<pad>']*(pad_length-len(tokens)))
        numbers=[token_to_idx.get(token,oov_num) for token in tokens]
        idxlist.append(numbers)
    return np.array(idxlist)
        
from torch import nn

class SentenceClassifier(nn.Module):
    def __init__(
            self,
            n_vocab,
            hidden_dim,
            embedding_dim,
            n_layers,
            feature_n,
            dropout=0.5,
            bidirectional=True,
            model_type='lstm'
            ):
        super().__init__()

        self.embedding=nn.Embedding(
            num_embeddings=n_vocab,
            embedding_dim=embedding_dim,
            padding_idx=0
        )
        if model_type=='rnn':
            self.model=nn.RNN(
                input_size=embedding_dim,
                hidden_size=hidden_dim,
                num_layers=n_layers,
                bidirectional=bidirectional,
                dropout=dropout,
                batch_first=True
            )
        elif model_type=='lstm':
            self.model=nn.LSTM(
                input_size=embedding_dim,
                hidden_size=hidden_dim,
                num_layers=n_layers,
                bidirectional=bidirectional,
                dropout=dropout,
                batch_first=True   
            )
        
        if bidirectional:
            self.classifier=nn.Linear(hidden_dim*2,feature_n)
        else:
            self.classifier=nn.Linear(hidden_dim,feature_n)
        self.dropout=nn.Dropout(dropout)

    def forward(self,inputs):
        embeddings=self.embedding(inputs)
        output,_=self.model(embeddings)
        last_output=output[:,-1,:]
        last_output=self.dropout(last_output)
        logits=self.classifier(last_output)
        return logits
    
class Train_val():
    def __init__ (self,trainDL,model,optimizer,lossF,scoreF):
        self.trainDL=trainDL
        self.model=model
        self.lossF=lossF
        self.scoreF=scoreF
        self.optimizer=optimizer
    
    def train(self,EPOCH,scheduler,modelnum):
        HISTORY={'loss':[[],[]],'score':[[],[]]}

        self.model.train()
        for epoch in range(EPOCH):

            loss_total=0
            score_total=0

            for feature,target in self.trainDL:
                feature=feature.to(device)
                target=target.to(device)

                pre_y=self.model(feature)
                logits=pre_y.logits
                loss=self.lossF(logits,target.reshape(-1).long())
                #logits=logits.detach().numpy()
                score=self.scoreF(logits,target.reshape(-1))

                self.optimizer.zero_grad()
                loss.backward()
                self.optimizer.step()

                loss_total+=loss.item()
                score_total+=score.item()

            HISTORY['loss'][0].append(loss_total/len(self.trainDL))
            HISTORY['score'][0].append(score_total/len(self.trainDL))

            # self.model.eval()
            # with torch.no_grad():
            #     for feature,target in self.valDL:
            #         val_pre_y=self.model(feature)

            #         loss=self.lossF(val_pre_y,target.reshape(-1).long())
            #         score=self.scoreF(val_pre_y,target.reshape(-1))
                
            #     HISTORY['loss'][1].append(loss.item())
            #     HISTORY['score'][1].append(score.item())
            

            # 모델 폴더가 없다면 생성
            if not os.path.exists('model/'):
                os.mkdir('model/')


            # trin score가 최고 인점 저장
            if len(HISTORY['score'][0])==1:
                torch.save(self.model,f'model/best_model{modelnum}.pth')
                #torch.save(self.model.state_dict(),f'model/best_weight{modelnum}.pth')
        
            elif HISTORY['score'][0][-1]>=min(HISTORY['score'][1]):
                torch.save(self.model,f'model/best_model{modelnum}.pth')
                #torch.save(self.model.state_dict(),f'model/best_weight{modelnum}.pth')


            
            
            print(f'[{epoch+1}/{EPOCH}]')
            print(f"train loss {HISTORY['loss'][0][-1]}, train score {HISTORY['score'][0][-1]}")
            #print(f"test loss {HISTORY['loss'][1][-1]}, test score {HISTORY['score'][1][-1]}")

            # test score 기준으로  scheduler 생성

            scheduler.step(HISTORY['score'][0][-1])
            print(f'scheduler.num_bad_epochs { scheduler.num_bad_epochs}/{ scheduler.patience}')

            if scheduler.num_bad_epochs >= scheduler.patience:
                print(f'[{scheduler.patience}] EPOCH 성능개선이 없어서 조기 종료함')
                break

        return HISTORY


from torch.utils.data import Dataset

class MyDataSet(Dataset):
    def __init__(self,feature,target):
        """ feature 와 target 이 DataFrame 일때"""
        super().__init__()
        self.feature=feature
        self.target=target
        self.n_rows=feature.shape[0]

    def __len__(self):
        return self.n_rows
    
    def __getitem__(self,index):
        featureTS=torch.tensor(self.feature.iloc[index].values)
        targetTS=torch.tensor(self.target.iloc[index].values)
        return featureTS,targetTS