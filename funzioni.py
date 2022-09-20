#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 20 19:18:52 2022

@author: giuseppe
"""

#foglio funzioni 

#conta elementi nell'array
def count_np(array):
    element = 0
    #ciclo for conta numero di elementi nell'array
    for i in array:
        element +=1
        
    return element

def somma(a,b):
    return a+b


#definisci numero primo
def prime_num(n):
    if n%2:
        return True
    return False


#calcola numeri primi 

def prime_calc(n):
    prime_list = []
    for i in range(0,n):
        if prime_num(i) == True:
            prime_list.append(i)
        else:
            i+=1
    return prime_list









