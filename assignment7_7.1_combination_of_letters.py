# -*- coding: utf-8 -*-
"""
Created on Thu Jul  2 17:49:28 2020

@author: Chennakesava Reddy
"""

#1.Write a Python program to create and display all combinations of letters, selecting each letter from a different key in a dictionary.
import itertools      
d ={'1':['a','b'], '2':['c','d']}
for combo in itertools.product(*[d[k] for k in sorted(d.keys())]):
    print(''.join(combo))


