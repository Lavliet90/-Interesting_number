#!/usr/bin/env python
# coding: utf-8

# In[1]:


'''Let's call a number interesting if the difference between the maximum and minimum 
digits in it is equal to the average digit. Write a program that detects an interesting 
number or not. If the number is interesting, you should print - "The number is interesting" 
otherwise "The number is not interesting".

Input data format
The input to the program is a three-digit integer number.

Output data format
The program should display the text in accordance with the condition of the problem.
'''
a=int(input())
b=a//100
c=(a//10)%10
d=a%10
k=min(b,c,d)
l=max(b,c,d)
s=(d+b+c)-(k+l)
if s==l-k:
    print("Число интересное")
else:
    print("Число неинтересное")


# In[ ]:




