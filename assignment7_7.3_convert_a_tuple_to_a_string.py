# -*- coding: utf-8 -*-
"""
Created on Thu Jul  2 18:03:38 2020

@author: Chennakesava Reddy
"""


#3.Write a Python program to convert a tuple to a string

def convertTuple(tup): 

    str =  ''.join(tup) 

    return str

  
# Driver code 

tuple = ('w', 'a', 'r', 'r', 'i','o','r') 

str = convertTuple(tuple) 

print(str)