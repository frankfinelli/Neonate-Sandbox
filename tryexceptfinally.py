# -*- coding: utf-8 -*-
"""
Created on Thu Dec 24 17:24:23 2015

@author: MOBIUS
"""
# try, except, finally

ui = 0
while True:
    try:
        ui = int(input('Enter a number :'))
    except ValueError:
        print ('not an integer')
    else:
        print ('you have entered a number')
        break
    break
