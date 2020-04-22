#!/usr/bin/env python
# coding: utf-8

# # Nesting Depth in Python

# ##### Test 1 - 0000,(1)0(1), (111)000, (1)
# ##### Test 2 - 0((2)1), (((3))1(2)), ((((4)))), ((2))0(((3))), ((2))((2))(1)

# In[6]:


m = input("Enter digits between - 0 to 9\n")
m = [int(i) for i in m]
n = []

for i in m: 
    
    if (n.count('(')-n.count(')'))<=i:
        while (n.count('(')-n.count(')')) != i:
            n.append('(')            
        n.append(i)        
        
    elif  (n.count('(')-n.count(')'))>i:
        while (n.count('(')-n.count(')'))!=i:
            n.append(')')
        n.append(i)    
        
while (n.count('(')-n.count(')'))!=0:
    n.append(')')
    
print(''.join(map(str, n)))

