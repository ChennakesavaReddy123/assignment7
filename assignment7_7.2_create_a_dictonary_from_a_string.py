# -*- coding: utf-8 -*-
"""
Created on Thu Jul  2 17:57:39 2020

@author: Chennakesava Reddy
"""
# Write a Python program to create a dictionary from a string.
from collections import defaultdict, Counter
str1 = 'chenna' 
my_dict = {}
for letter in str1:
    my_dict[letter] = my_dict.get(letter, 0) + 1
print(my_dict)
