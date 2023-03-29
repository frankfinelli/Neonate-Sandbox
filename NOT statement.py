# -*- coding: utf-8 -*-
"""
Created on Mon Dec  7 19:18:18 2015

@author: MOBIUS
"""

#NOT statement#
a = 0
b = 2

while a < 11:
    if not a%b:
        print (str(a) + '-->' + 'even')
    if a%b:
        print (str(a) + '-->' + 'odd')
    a += 1