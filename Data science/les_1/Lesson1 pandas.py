#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


a = [2, 4, 6, 8]


# In[3]:


b = pd.Series(a)
b


# In[5]:


b.head()


# In[6]:


b.head(3)


# In[7]:


b.tail()


# DataFrame

# In[12]:


df = pd.DataFrame({'Col1':['a', 'b', 'c'],
                  'Col2':[1, 2, 3]}, columns = ['Col1', 'Col2'])
df


# In[14]:


df.describe()


# In[15]:


#слияние данных
authors = pd.DataFrame({'author_id':[1, 2, 3], 'author_name':['Pushkin', 'Tolstoy', 'Dostoevsky']},
                      columns = ['author_id', 'author_name'])
authors


# In[16]:


books = pd.DataFrame({'author_id':[2,3,3,4],
                     'book_title':['War and Peace', 'The idiot', 'Crime and Punishment', 'Fathers and sons']})
books


# In[17]:


df1 = pd.merge(authors, books, on='author_id', how='inner')
df1


# In[18]:


df2 = pd.merge(authors, books, on='author_id', how='left')
df2


# In[19]:


df3 = pd.merge(authors, books, on='author_id', how='right')
df3


# In[ ]:




