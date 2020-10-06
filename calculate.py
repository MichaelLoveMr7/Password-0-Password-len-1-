#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  5 14:33:24 2020

@author: yujiedong
"""

import glob
import os
import pandas as pd



os.chdir("/Users/yujiedong/Downloads/BreachCompilation/data/New_0andLast/combined")

extension = 'csv'

all_filenames = [i for i in glob.glob('*.{}'.format(extension))] # ?
# combine all files in the list
combined_csv = pd.concat([pd.read_csv(f) for f in all_filenames])

data = combined_csv.iloc[:,1:3]
data = data.reset_index(drop=True)

length=(len(data))
row = 0
N1ALL_SUM = 0
N3ALL_SUM = 0
U1ALL_SUM = 0
U3ALL_SUM = 0
S1ALL_SUM = 0
S3ALL_SUM = 0
count_users = 0

'''
count = 0
while(count < length):
    if data.iloc[count,0] == 'count_odd_even':
        print('count_odd_even:',data.iloc[count, 1])
        count_users = count_users + data.iloc[count,1]
        
    count = count + 1
#print("finally:", count_users)    
 '''  
while(row < length):
    if data.iloc[row,0] == 'count_odd_even':
        count_users = count_users + data.iloc[row,1]
    
    if data.iloc[row,0] == 'N1ALL':
        N1ALL_SUM = N1ALL_SUM + data.iloc[row,1]
        
    if data.iloc[row,0] == 'N3ALL':
        N3ALL_SUM = N3ALL_SUM + data.iloc[row,1]
        
    if data.iloc[row,0] == 'U1ALL':
        U1ALL_SUM = U1ALL_SUM + data.iloc[row,1]
        
    if data.iloc[row,0] == 'U3ALL':
        U3ALL_SUM = U3ALL_SUM + data.iloc[row,1]
        
    if data.iloc[row,0] == 'S1ALL':
        S1ALL_SUM = S1ALL_SUM + data.iloc[row,1]
        
    if data.iloc[row,0] == 'S3ALL':
        S3ALL_SUM = S3ALL_SUM + data.iloc[row,1]
        
    row = row + 1  
print('count_users:',count_users)  

count_users = ['User_count_SUM:',count_users]
N1ALL_SUM = ['N_password[0]:',N1ALL_SUM]
N3ALL_SUM = ['N_password[length-1]:',N3ALL_SUM]
U1ALL_SUM = ['U_password[0]:',U1ALL_SUM]
U3ALL_SUM = ['U_password[length-1]:',U3ALL_SUM]
S1ALL_SUM = ['S_password[0]:',S1ALL_SUM]
S3ALL_SUM = ['S_password[length-1]:',S3ALL_SUM]

import numpy as np
np.savetxt('1.4B_pass[0]ANDpass[len-1].csv', (  
                count_users ,
                N1ALL_SUM ,
                N3ALL_SUM ,
                U1ALL_SUM ,
                U3ALL_SUM ,
                S1ALL_SUM ,
                S3ALL_SUM 

    ), fmt='%s')
result_data=pd.read_csv('1.4B_pass[0]ANDpass[len-1].csv',sep=":",header = None)
result_data.to_csv('1.4B_pass[0]ANDpass[len-1].csv')
    
    
    
    
    