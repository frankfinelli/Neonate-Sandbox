# -*- coding: utf-8 -*-
"""
Created on Fri Nov 27 21:07:43 2015

@author: MOBIUS
"""

##PRIME PRACTICE##

x = 0
x == 0
for p in range(2,str(x)+1):
    for i in range(2,p):
        if p%i == 0:
            break    # <== break here (when a factor is found)
    else:            # <==else belongs to the for, not the if
        print (p)

print ("Done")