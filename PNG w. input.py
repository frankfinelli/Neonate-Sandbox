# -*- coding: utf-8 -*-
"""
Created on Fri Nov 27 21:09:17 2015

@author: MOBIUS
"""

##prime generator using user input##

x = input("Enter a number: ")
for p in range(2,int(x)+1):
    for i in range(2,p):
        if p%i == 0:
            break    # <== break here (when a factor is found)
    else:            # <==else belongs to the for, not the if
        print (p)

print ("Done")

