# -*- coding: utf-8 -*-
"""
Created on Fri Dec  4 20:40:24 2015

@author: Franco Finelli
"""

#png loop w. output write to text file#

file = open('listoprimes.txt', 'w')

a = 2
while (a > 1):
    b = 2
    while (b <= (a/b)):
        if not (a%b):
            break
        b += 1
    if (b > a/b):
        print (a)
        file.write (str(a) + '\n')
    a += 1