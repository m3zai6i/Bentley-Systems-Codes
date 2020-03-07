# -*- coding: utf-8 -*-
"""
===================
Question Statement
===================

Input: 'aaaabbbb'
Output: 1

Output is number of character(s) that is removed so that every character have
unique number of letters e.g. Remove 'a',a=3,b=4

@author: Shahzaib Asif
"""
# initializing string 
test_str = "aaaabbbb"

all_freq = {} 
count = 0
minus = 0
c1 = 0
c2 = 0
for i in test_str:
	if i in all_freq: 
		all_freq[i] += 1
		c1 +=1
	else: 
		all_freq[i] = 1
		count = count + minus
		minus = minus + 1
		c2 +=1

print("Count of all characters is : "+str(all_freq))

print('Output:',count)

