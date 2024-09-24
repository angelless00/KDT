import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.utils.data import Dataset




class DynamicsModel(nn.Module):
    def __init__(self,in_in,out_out_,nums=[]):
        super().__init__()
        self.in_layer=nn.Linear(in_in,nums[0] if len(nums) else 5)
        self.h_layer=nn.ModuleList()
        for n in range(len(nums)-1):
            self.h_layer.append(nn.Linear(nums[n],nums[n+1]))
        self.out_layer=nn.Linear(nums[-1] if len(nums) else 5)

    def forward(self,x):
        x=F.relu(self.in_layer(x))
        for module in self.h_layer:
            x=F.relu(module(x))
        return self.out_layer(x)
    

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
        featureTS=torch.FloatTensor(self.feature.iloc[index].values)
        targetTS=torch.FloatTensor(self.target.iloc[index].values)



