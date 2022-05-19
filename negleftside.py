#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 19 21:10:34 2022

@author: koushik
"""
def negleftside(a):
    j=0
    for i in range(0,len(a)):
        if(a[i]<0):
            temp=a[i]
            a[i]=a[j]
            a[j]=temp
            j=j+1
a=[-1,2,-3,4]
negleftside(a)
print(a)
            