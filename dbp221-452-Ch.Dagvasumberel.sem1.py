#!/usr/bin/env python
# coding: utf-8

# In[1]:


#1-р даалгавар
a=["python","php","java"]
print(a[0])
print(a[1])
print(a[2])


# In[2]:


#2-р даалгавар
a=[1,2,3,4,5,6,7,7,8,9,]
b=0
for i in a:
    b=i+b
print(b)


# In[3]:


#3-р даалгавар
def multiply(x):
    b = 1
    for i in x:
        b = b * i
    return b


# In[4]:


#3-р даалгавар шалгасан нь 
x=[123,124,125,126,127]
print(multiply(x))


# In[5]:


#4-р даалгавар
def multiply1(a):
    y=1
    for i in a:
        y=a[2]*a[-1]
    return y


# In[6]:


#4-р даалгавар шалгасан нь
a=[1,2,3,4,55,5,5,6,6,7]
print(multiply1(a))


# In[7]:


#5-р даалгавар
def ihtoo(a):
    x=max(a)
    return x

def bagatoo(a):
    y=min(a)
    return y


# In[8]:


#5-р даалгавар шалгасан нь
a=[1,2,3,4,55,5,5,6,6,7]
print("Хамгийн их тоо",ihtoo(a))
print("Хамгийн бага тоо",bagatoo(a))


# In[9]:


#6-р даалгавар
a=['abdba', 'abcd', '121','7171717171','11111101010119999191']
x=0
for y in a:
    if len(y)>2 and y[0]==y[-1]:
        x=x+1
print(x)


# In[10]:


#7-р даалгавар
def dawhardsan_utga(a):
    return list(dict.fromkeys(a))
mylist = dawhardsan_utga(['abdba', 'abcd', 121, 121, 'abcd','barathrum','barathrum','glordindel','Glorfindel'])
print(mylist) 


# In[11]:


#8-р даалгавар
def hooson(a):
    if len(a):
        print('not empty')
    else:
        print('empty')
a=['12','1212']
hooson(a)    


# In[12]:


#9-р даалгавар
a=[12,13,14,15,16,17,18,19,20,21]
del a[3]
del a[4]
del a[5]
print(a)


# In[13]:


#10-р даалгавар
a=(11,12,13,14,15,16,17,18,19,20)


# In[14]:


#11-р даалгавар
a=(11,12,13,14,15,16,17,18,19,20)
b=list(a)
b.append(33)
a=tuple(b)
print(a)


# In[15]:


#12-р даалгавар
a=(11,12,13,14,15,16,17,18,19,20)
b=list(a)
print(b[1],b[-2])


# In[16]:


#13-р даалгавар
tuple1= ('x','y','z','m','n','d')
utga= input('Утгаа оруул: ')
for ch in tuple1:
    if ch ==utga:
        print('Tuple-д байна.')
        break
    else:
        print('Tuple-д алга.')
        break


# In[17]:


#14-р даалгавар
tuple1= ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h')
for i in tuple1:
    print(i)


# In[18]:


#15-р даалгавар
a={'1','2','3','4'}
b={'5','6','7','8'}
print(a.union(b))


# In[19]:


#16-р даалгавар
a={'1','2','3','5'}
b={'5','6','3','8'}
print(a.intersection(b))


# In[20]:


#17-р даалгавар
a={'1','2','3','5'}
print(len(a))


# In[21]:


#18-р даалгавар
a={'1','2','3','5','5','6','3','8'}
utga=input()
a.discard(utga)
print(a)


# In[22]:


#19-р даалгавар
a={'1','2','3','5','5','6','3','8'}
a.clear()
print(a)


# In[ ]:


#20-р даалгавар
a={'1','2','3','5','5','6','3','8'}
del a



# In[23]:


#21-р даалгавар
dict1={'12':144,'3':9,'15':225,'4':16,'21':441}
a = sorted(dict1.items(), key=lambda x: x[1])    #интернэтээс санаа авав.
print(a)


# In[24]:


#22-р даалгавар
dict2={12:144,3:9,15:225,4:16,21:441}
x=int(input())
if x in dict2:
    print(x,' dict-д байна.')
else:
    print(x,' dict-д алга')


# In[25]:


#23-р даалгавар
dict2={12:144,3:9,15:225,4:16,21:441}
x=int(input())
if x in dict2.values():
    print(x,' dict-д байна.')
else:
    print(x,' dict-д алга')


# In[26]:


#24-р даалгавар
dict4 = {12:144,3:9,15:225,4:16,21:441}
for i in dict4:
    print(i,dict4[i])


# In[27]:


#25-р даалгавар
dict6 = {12:144,3:9,15:225,4:16,21:441}
dict5 = { 'Manufacturer': 'Tesla', 'Model': '3', 'Year': 2021 } 
dict6.update(dict5)
print(dict6)


# In[28]:


#26-р даалгавар
dict7 = {12:144,3:9,15:225,4:16,21:441}
sum = 0
for i in dict7:
    sum = sum + dict7[i]
print("Нийлбэр:",sum)


# In[29]:


#B20FA1108 Ch.Dagvasumberel DBP221-452
print('DONE')


# In[ ]:




