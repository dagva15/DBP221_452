#!/usr/bin/env python
# coding: utf-8

# In[22]:


# 1-р даалгавар
def palindrome(a):
    x=a
    r=0
    while a>0:
        b=a%10
        r=r*10+b
        a=a//10
    if x==r:
        print('It is palindrome number')
    else:
        print('It is not palindrome number')
a=int(input())
palindrome(a)


# In[21]:


# 1-р даалгавар
def Palindrome(s):
    rev = ''.join(reversed(s))
    if (s == rev):
        return True
    return False
 
s =input()
ans=Palindrome(s)
 
if (ans):
    print("It is Palindrome number")
else:
    print("It is not Palindrome number")


# In[19]:


# 2-р даалгавар
def tomjijiguseg(x):
    tom=0
    jijig=0
    for i in range(len(x)):
        if(x[i] >='A' and x[i] <='Z'):
            tom+=1
        elif(x[i] >='a' and x[i] <='z'):
            jijig+=1
    return [tom,jijig]
x=['A','B','c','d','D','Y','o']
print(tomjijiguseg(x))


# In[ ]:


# 3-р даалгавар
def urjver(x):
    a=1
    for i in x:
        a=a*i
    return a
list1=[2,3,4,5,6,7,8,9,10]
print(urjver(list1))


# In[14]:


# 4-р даалгавар
def factorial(x):
    a=1
    while x>0:
        a=x*a
        x=x-1
    return a
x=int(input())
print(factorial(x))


# In[15]:


# 5-р даалгавар
def rev(x):
    list1.reverse()
    return x
list1=['uher','honi','mori','temee','ymaa']
print(rev(list1))


# In[25]:


# 6-р даалгавар
def sum(x):
    a=0
    for i in x:
        a+=i
    return a
list1=[1,2,3,4,4,4,4,4,4,4,5]
print(sum(list1))
        


# In[3]:


# 7-р даалгавар
def D_utga(x):
    s=set(x)
    l=list(s)
    return l
Mylist=['a','b','c','c','c','b','b','e','t','e']
print(D_utga(Mylist))


# In[42]:


# 8-р даалгавар
def maximum(a, b, c):
    if (a >= b) and (a >= c):
        largest = a
    elif (b >= a) and (b >= c):
        largest = b
    else:
        largest = c
    return largest
a = int(input())
b = int(input())
c = int(input())
print('Хамгийн их тоо нь:',maximum(a, b, c))
            


# In[4]:


print("Done")


# In[ ]:




