# -*- coding: utf-8 -*-
"""
Created on Fri Nov 27 21:02:18 2015

@author: MOBIUS
"""

##I/O using math and if/then##
print("Pick a word that has 12 letters")
word1=input()
quant1=float(int(len(word1)))
if quant1 == 12:
    print("Good work! You know how to count!")
else:
    print("Fool! You should\'ve picked the word \"niggerfaggot\". Try again:")
    word2=input()
    quant2=float(int(len(word2)))
    if word2 == str("niggerfaggot") and quant2 == 12:
        print("Well done; you understand English, dipshit!")
    if quant2 == 12 and word2 != str("niggerfaggot"):
        print("Good job picking a twelve letter word, you fuckhead!")
    if quant2 != 12:
        print("Kill yourself and rid your genes from the pool, faggot!")