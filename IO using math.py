# -*- coding: utf-8 -*-
"""
Created on Fri Nov 27 20:54:54 2015

@author: MOBIUS
"""

##I/O using math##
stack='Type a word that has letters'
print(stack)
word=input()
downs=(len(word))
upsie=int(downs)
leftloose=int(abs(upsie-6))
print('Your word has '+ str(upsie) + ' letters in it.')
print('If you picked the word \"faggot\" you would have been ' + str(leftloose) + ' letters away!')