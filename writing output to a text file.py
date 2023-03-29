# -*- coding: utf-8 -*-
"""
Created on Fri Dec  4 20:33:17 2015

@author: MOBIUS
"""

#Writing output to a text file#
file = open('newfile.txt', 'w')
file.write("hello world\n")
file.write('and another line\n')
file.close()
