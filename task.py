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
while j < data.shape[0]:
    num1 = 2*(data['q0'][j]*data['q1'][j]+data['q2'][j]*data['q3'][j])
    den1 = 1-(2*(data['q1'][j]*data['q1'][j]+data['q2'][j]*data['q2'][j]))

    roll.append( np.arctan(num1 / den1) )

    pitch.append( np.arcsin( 2*(data['q0'][j]*data['q2'][j]-data['q1'][j]*data['q3'][j])) )

    num2 = 2*(data['q0'][j]*data['q3'][j]+data['q1'][j]*data['q2'][j])
    den2 = 1-(2*(data['q3'][j]*data['q3'][j]+data['q2'][j]*data['q2'][j]))

    yaw.append( np.arctan( num2 / den2) )

    j+=1

plt.plot(data['time'],roll)
plt.show()
plt.plot(data['time'],pitch)
plt.show()
plt.plot(data['time'],yaw)
plt.show()
