# 모듈로딩

import os
import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.utils.data import Dataset,DataLoader
import torch.optim as optim
from torchmetrics.classification import MulticlassF1Score,F1Score
import matplotlib.pyplot as plt

class AlphaMCFModel(nn.Module):
    def __init__(self,in_in,out_out,n1,n2):
        super().__init__()
        self.in_layer=nn.Linear(in_in,n1)
        self.h_layer=nn.Linear(n1,n2)
        self.out_layer=nn.Linear(n2,out_out)

    def forward(self,x):
        x=F.relu(self.in_layer(x))
        x=F.relu(self.h_layer(x))
        return self.out_layer(x)
    


# 그림그리는 함수
class LossScorePlot():
    def __init__(self,loss,score):
        self.loss=loss
        self.score=score

    def LSplot(self):
        fig,ax=plt.subplots(1,2,figsize=(10,5))
        ax[0].plot(self.loss,label='train')
        ax[0].grid()
        ax[0].set(xlabel='EPOCH',ylabel='loss')
        ax[0].legend()

        ax[1].plot(self.score,label='train')
        ax[1].grid()
        ax[1].set(xlabel='EPOCH',ylabel='score')
        ax[1].legend()
        plt.show()