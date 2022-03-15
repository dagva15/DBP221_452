#!/usr/bin/env python
# coding: utf-8

# In[59]:


def odtoitoo(n):
    n=int(input())
    a=1
    while a<n+1:
        print('*'*a)
        a+=1
odtoitoo(8)


# In[2]:


# 2-р даалгавар
def listteiod(n):
    n=int(input())
    a=1
    while a<n+1:
        print(['*'*a])
        a+=1
listteiod(7)


# In[3]:


# 3-р даалгавар
def ihbaga(students):
    a= max(students, key=students.get)
    b= min(students, key=students.get)
    return a,b
students = {'Bat': 1000,'Oyun': 1001,'Dulam': 999,'Suren':1000}
ihbaga(students)


# In[22]:


import numpy as np


# In[53]:


# 4-р даалгавар
a=np.arange(1,1000)
b=0
for i in a:
#     b=0
    if i%3==0 or i%7==0:
        b=b+i
print(b)


# In[54]:


print("DONE")


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




