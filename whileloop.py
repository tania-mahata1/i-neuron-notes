#!/usr/bin/env python
# coding: utf-8

# In[10]:


lst=[1,2,3,4,5,6,7]
lst


# In[11]:


even=0
odd=0
for i in lst:
    if i%2==0:
        even=even+i
        if even>20:
            break
            
    else:
        odd=odd+i
        if odd>20:
            break
else:
    print(even,"  sum of even")
    print(odd, "  sum  of odd")   


# In[12]:


even=0
odd=0
i=1
n=10
while i<=n:
    if i%2==0:
        even=even+i
        i=i+1
    else:
        odd=odd+i
        i=i+1
print(even)
print(odd)
        


# In[13]:


range(0,100)


# In[15]:


list(range(0,100))


# In[16]:


s="Tania is a good girl"
s


# In[17]:


s.upper()


# In[18]:


s.capitalize()


# In[22]:


s.center(30,'-')


# In[23]:


s="h i  o i u  y"
s.isspace()


# In[24]:


"tania\tmahata"


# In[25]:


"tania\tmahata".expandtabs()


# In[26]:


n=5
i=1
while i<=n:
    print(i)
    i=i+1


# In[28]:


sum(range(1,10,2))


# In[29]:


lst


# In[30]:


lst.pop(4)


# In[31]:


lst


# In[32]:


lst.pop(3)


# In[33]:


lst


# In[ ]:




