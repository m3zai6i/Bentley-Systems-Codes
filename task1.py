# -*- coding: utf-8 -*-
"""
===================
Question Statement
===================
Input: 1 4 2 5
Output: 2

Output at that point which both left and right array sum are equal e.g. {1,4},{5}

@author: Shahzaib Asif
"""

s = input('Enter Number: ')
size = len(s)
output = ''

for i in range(1,size-1):
    
    sum1=0
    sum2=0
    
    for j in range(0,i):
        sum1 = sum1 + int(s[j])
        #print('sum1=',sum1)
        
    for k in range(i+1,size):
        sum2 = sum2 + int(s[k])
        #print('sum2=',sum2)
        
    if (sum1==sum2):
        output = s[i]
        
print('Output =',output)

