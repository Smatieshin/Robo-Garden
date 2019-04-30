# -*- coding: utf-8 -*-
"""
Created on Tue Apr 30 11:47:17 2019

@author: Scott
"""
numsum = 0  #set sum to zero
numlist = []  # create empty list
for x in range(5):  # loop five times
    y = int(input('Enter a number between 0 and 20 '))
    numlist.insert(x,y)  #insert input value y to list at x
    numsum = numsum + y # running total of inputs
if numsum >= 85:
    finalgrade = 'A'
elif numsum >= 75:
    finalgrade = 'B'
elif numsum >= 65:
    finalgrade = 'C'
elif numsum >= 50:
    finalgrade = 'D'
else:
    finalgrade = 'F'
print('Grades from assignments', numlist)
print('Final number grade ', numsum)    
print('Final Letter Grade ', finalgrade)