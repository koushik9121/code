#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 12 12:29:12 2022

@author: koushik
"""
def maxelem(A,n):
    max=A[0]
    for i in range(1,n):
        if A[i] > max:
            max=A[i]
    return max        
A=[1,2,3]
n=len(A)
s=maxelem(A,n)
print(s)        


