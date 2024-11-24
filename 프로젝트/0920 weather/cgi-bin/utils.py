import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.utils.data import Dataset
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt 

# 데이터셋 분리
class SeperateSet():
    def __init__(self,feature,target):
        self.feature=feature
        self.target=target
    
    def run(self):
        ''' output= X_train,X_val,X_test,y_train,y_val,y_test '''
        X_train,X_test,y_train,y_test=train_test_split(self.feature,self.target,test_size=0.2,random_state=1)
        X_train,X_val,y_train,y_val=train_test_split(X_train,y_train,test_size=0.2,random_state=1)
        return X_train,X_val,X_test,y_train,y_val,y_test

    

class DynamicsModel(nn.Module):
    def __init__(self,in_in,out_out,nums=[]):
        super().__init__()
        self.in_layer=nn.Linear(in_in,nums[0] if len(nums) else 5)
        self.h_layer=nn.ModuleList()
        for n in range(len(nums)-1):
            self.h_layer.append(nn.Linear(nums[n],nums[n+1]))
        self.out_layer=nn.Linear(nums[-1] if len(nums) else 5,out_out)

    def forward(self,x):
        x=F.relu(self.in_layer(x))
        for module in self.h_layer:
            x=F.relu(module(x))
        return self.out_layer(x)
    


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
                loss=self.lossF(pre_y,target)
                score=self.scoreF(pre_y,target)

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

                    loss=self.lossF(val_pre_y,target)
                    score=self.scoreF(val_pre_y,target)
                
                HISTORY['loss'][1].append(loss.item())
                HISTORY['score'][1].append(score.item())

            # val loss가 최저인점 저장
            if len(HISTORY['loss'][1])==1:
                torch.save(self.model,f'model/best_model{modelnum}.pth')
                torch.save(self.model.state_dict(),f'model/best_weight{modelnum}.pth')
        
            elif HISTORY['loss'][1][-1]<=min(HISTORY['loss'][1]):
                torch.save(self.model,f'model/best_model{modelnum}.pth')
                torch.save(self.model.state_dict(),f'model/best_weight{modelnum}.pth')


        
            
            print(f'[{epoch+1}/{EPOCH}]')
            print(f"train loss {HISTORY['loss'][0][-1]}, train score {HISTORY['score'][0][-1]}")
            print(f"val loss {HISTORY['loss'][1][-1]}, val score {HISTORY['score'][1][-1]}")

            scheduler.step(HISTORY['loss'][1][-1])
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
        final=len(self.history)
        axs[0].plot(range(1 if num==0 else final-num+1 ,final+1),self.history['loss'][0][-1*num:],label='train')
        axs[0].plot(range(1 if num==0 else final-num+1 ,final+1),self.history['loss'][1][-1*num:],label='val')
        axs[0].set(xlabel='EPOCH',ylabel='loss')
        axs[0].grid()
        axs[0].legend()

        axs[1].plot(range(1 if num==0 else final-num+1 ,final+1),self.history['score'][0][-1*num:],label='train')
        axs[1].plot(range(1 if num==0 else final-num+1 ,final+1),self.history['score'][1][-1*num:],label='val')
        axs[1].set(xlabel='EPOCH',ylabel='score')
        axs[1].grid()
        axs[1].legend()




class DropDynamicsModel(nn.Module):
    def __init__(self,in_in,out_out,nums=[]):
        super().__init__()
        self.in_layer=nn.Linear(in_in,nums[0] if len(nums) else 5)
        self.h_layer=nn.ModuleList()
        for n in range(len(nums)-1):
            self.h_layer.append(nn.Linear(nums[n],nums[n+1]))
            self.dropout=nn.Dropout(0.5)
        self.out_layer=nn.Linear(nums[-1] if len(nums) else 5,out_out)

    def forward(self,x):
        x=F.relu(self.in_layer(x))
        for module in self.h_layer:
            x=F.relu(module(x))
            x=self.dropout(x)
        return self.out_layer(x)
    