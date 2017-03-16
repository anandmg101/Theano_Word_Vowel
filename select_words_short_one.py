# -*- coding: utf-8 -*-
"""
Created on Tue Feb 28 09:01:51 2017

@author: agnanamoorthy
"""
import csv

wf = open('output.txt', "w")

check_list = ['a', 'e', 'i', 'o', 'u', 't', 'l', 'f', 'b', 'k', 'w', 'n', 'm', 'h']
#final_list = []

with open('Words.csv') as csvfile:
    rf =  csv.reader(csvfile)
    for words in rf:
        for word in words:
            add = True
            for letter in word:
                if letter not in check_list: add = False
            if add and len(word) > 2:
                #print (word)
                #if not isinstance(word,list):
                wf.write(word)
                wf.write('\n')
        
wf.close()
        
