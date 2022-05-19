#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 12 14:58:56 2022

@author: koushik
"""
def Setarr(A):
    count=0
    count1=0
    for i in range(0,len(A)):
        if A[i]==0:
            count+=1
        elif A[i]==1:
            count1+=1
    for i in range(0,len(A)):
        if count!=0:
            A[i]=0
            count-=1
        elif count1!=0:
            A[i]=1
            count1-=1
        else:
            A[i]=2
A=[0,1,2,2,1,0]
Setarr(A)
print(A)
       
     