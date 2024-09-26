import torch
import torch.nn as nn
import matplotlib.pyplot as plt
import os 
import torch.functional as F

class MyDataSet(Dataset):
    def __init__(self,feature,target):
        """ feature 와 target 이 DataFrame 일때"""
        self.feature=feature
        self.target=target
        self.n_rows=feature.shape[0]

    def __len__(self):
        return self.n_rows
    
    def __getitem__(self,index):
        featureTS=torch.FloatTensor(self.feature.iloc[index].values)
        targetTS=torch.FloatTensor(self.target.iloc[index].values)
        return featureTS,targetTS


class CNNmodel(nn.Module):
    def __init__(self,kernel,out_out,shape,Knums=[10,5],Pnums=[10]):
        super().__init__()
        self.in_layer=nn.Sequential(
            nn.Conv2d(in_channels=kernel,out_channels=Knums[0],kernel_size=3,padding=1),
            nn.BatchNorm2d(Knums[0]),
            nn.ReLU(),
            nn.MaxPool2d(2))
        self.h_layer=nn.ModuleList()
        for n in range(len(Knums)-1):
            self.h_layer.append(nn.Sequential(
                nn.Conv2d(in_channels=Knums[n],out_channels=Knums[n+1],kernel_size=3,padding=1),
                nn.BatchNorm2d(Knums[n+1]),
                nn.ReLU(),
                nn.MaxPool2d(2)))
        self.fcs=nn.ModuleList()
        self.fcs.append(nn.Linear(int(((shape/(2**(len(Knums))))**2 )*Knums[-1]),Pnums[0]))
        self.fcs.append(nn.ReLU())
        for n in range(len(Pnums)-1):
            self.fcs.append(nn.Linear(Pnums[n],Pnums[n+1]))
            self.fcs.append(nn.ReLU())
        self.fcs.append(nn.Linear(Pnums[-1],out_out))
    
    def forward(self,x):
        x=self.in_layer(x)
        for module in self.h_layer:
            x=module(x)
        x=x.view(x.size(0),-1)
        for module in self.fcs:
            x=module(x)
        return x
    

class Train_val():
    def __init__ (self,trainDL,valDL,model,optimizer,lossF,scoreF):
        self.trainDL=trainDL
        self.valDL=valDL
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
                pre_y=self.model(feature)
                loss=self.lossF(pre_y,target.reshape(-1).long())
                score=self.scoreF(pre_y,target.reshape(-1))

                self.optimizer.zero_grad()
                loss.backward()
                self.optimizer.step()

                loss_total+=loss.item()
                score_total+=score.item()

            HISTORY['loss'][0].append(loss_total/len(self.trainDL))
            HISTORY['score'][0].append(score_total/len(self.trainDL))

            self.model.eval()
            with torch.no_grad():
                for feature,target in self.valDL:
                    val_pre_y=self.model(feature)

                    loss=self.lossF(val_pre_y,target.reshape(-1).long())
                    score=self.scoreF(val_pre_y,target.reshape(-1))
                
                HISTORY['loss'][1].append(loss.item())
                HISTORY['score'][1].append(score.item())
            

            # 모델 폴더가 없다면 생성
            if not os.path.exists('model/'):
                os.mkdir('model/')


            # val loss가 최저인점 저장
            if len(HISTORY['score'][1])==1:
                torch.save(self.model,f'model/best_model{modelnum}.pth')
                #torch.save(self.model.state_dict(),f'model/best_weight{modelnum}.pth')
        
            elif HISTORY['score'][1][-1]>=min(HISTORY['score'][1]):
                torch.save(self.model,f'model/best_model{modelnum}.pth')
                #torch.save(self.model.state_dict(),f'model/best_weight{modelnum}.pth')



            
            
            print(f'[{epoch+1}/{EPOCH}]')
            print(f"train loss {HISTORY['loss'][0][-1]}, train score {HISTORY['score'][0][-1]}")
            print(f"test loss {HISTORY['loss'][1][-1]}, test score {HISTORY['score'][1][-1]}")

            # score 기준으로  scheduler 생성

            scheduler.step(HISTORY['score'][1][-1])
            print(f'scheduler.num_bad_epochs { scheduler.num_bad_epochs}/{ scheduler.patience}')

            if scheduler.num_bad_epochs >= scheduler.patience:
                print(f'[{scheduler.patience}] EPOCH 성능개선이 없어서 조기 종료함')
                break

        return HISTORY

class Plot_History():
    def __init__(self,history):
        self.history=history


    def draw(self,num=0):
        fig,axs=plt.subplots(1,2,figsize=(10,5))
        final=len(self.history['loss'][0])
        axs[0].plot(range(1 if num==0 else final-num+1 ,final+1),self.history['loss'][0][-1*num:],label='train')
        axs[0].plot(range(1 if num==0 else final-num+1 ,final+1),self.history['loss'][1][-1*num:],label='test')
        axs[0].set(xlabel='EPOCH',ylabel='loss')
        axs[0].grid()
        axs[0].legend()

        axs[1].plot(range(1 if num==0 else final-num+1 ,final+1),self.history['score'][0][-1*num:],label='train')
        axs[1].plot(range(1 if num==0 else final-num+1 ,final+1),self.history['score'][1][-1*num:],label='test')
        axs[1].set(xlabel='EPOCH',ylabel='score')
        axs[1].grid()
        axs[1].legend()
        