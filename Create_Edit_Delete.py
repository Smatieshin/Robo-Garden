# -*- coding: utf-8 -*-
"""
Created on Fri May  3 14:52:45 2019

@author: Scott
Create, Edit, and Delete exercise - RoboGarden
"""
f = open('myfile.txt', 'w') # Create and open myfile.txt

l = ['hi', 'there', 'I', 'am', 'writing', 'in', 'a', 'file']

with open('myfile.txt', 'w') as f: #populate myfile.txt with list l
    for s in l:
       f.write(s + '\n')
       
with open('myfile.txt', 'r') as f: # print contents of myfile.txt
    for line in f:
        print(line, end='')       

with open('myfile.txt', 'a') as f:  #append 'bye' to myfile.txt
    f.write('Bye\n')

import os #delete myfile.txt
os.remove('myfile.txt')