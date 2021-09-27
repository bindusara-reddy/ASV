import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
with open('TC_1.9_0.7ms_1.txt','r') as file:
    string_list = file.readlines()
    i= 0
    while i < len (string_list):
        string_list[i] = string_list[i][:-1] + string_list[i+1]
        string_list.pop(i+1)
        i+=1
    with open('copy.txt','w') as copy:
        copy.writelines(string_list)
data=pd.read_csv('copy.txt')
#print(data)
roll = []
pitch = []
yaw = []
j=0
while j < len(string_list):
    roll[j] = np.arctan( (2*(data[2][j]*data[3][j]+data[4][j]*data[5][j]))/(1-(2*(data[3][j]*data[3][j]+data[4][j]*data[4][j]))))
    pitch[j] = np.arcsin( 2*(data[2][j]*data[4][j]-data[3][j]*data[5]))
    yaw[j] = np.arctan( (2*data[2][j]*dat[5][j]+data[3][j]*data[4][j])/(1-(2*(data[4][j]*data[4][j]+data[5][j]*data[5][j]))))

print(roll)
