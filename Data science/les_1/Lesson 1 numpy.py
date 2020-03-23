#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[2]:


a = np.array([i for i in range(10)])


# In[4]:


print(a)


# In[8]:


b = np.array(a, dtype = float)


# In[9]:


b.ndim #размерность массива


# In[10]:


b.shape


# In[12]:


# 2D array
c = np.array([[0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
             [10, 11, 12, 13, 14, 15, 16, 17, 18, 19],
             [20, 21, 22, 23, 24, 25, 26, 27, 28, 29]])


# In[13]:


c


# In[14]:


c.shape


# In[16]:


c.size


# линейная алгебра

# In[18]:


a = np.array([0, 1, 2, 3, 4])


# In[19]:


b = np.array([5, 6, 7, 8, 9])


# In[21]:


c = np.add(a, b) #сложение
print(c)


# In[24]:


c = np.subtract(a, b) #вычитание
print(c)


# In[25]:


#умножение
#вариант 1
a.dot(-10)


# In[26]:


#вариант 2
np.dot(-10, a)


# In[27]:


#вариант 3
np.multiply(-10, a)


# In[28]:


#скалярное произведение векторов
#вариант 1
a @ b


# In[30]:


#вариант 2
sp = np.dot(a, b)
sp


# In[31]:


#операции с матрицами


# In[32]:


A = ([[0, 1],
     [2, 3],
     [4, 5]])
B = ([[6, 7],
     [8, 9],
     [10, 11]])


# In[34]:


C = np.add(A, B) #сложение матриц
C


# In[35]:


C = np.subtract(A, B) #вычитание матриц
C


# In[37]:


#умножение матриц
x1 = np.array([[1,2], [3,4], [5,6]])
x2 = np.array([[1, 2, 3, 4],[5, 6, 7, 8]])
x1.shape[1] == x2.shape[0]


# In[39]:


z = np.dot(x1, x2)
z


# In[40]:


#возведение матрицы в квадрат
A = np.array([[0, 1, 2],
             [3, 4, 5],
             [6, 7, 8]])
A2 = np.linalg.matrix_power(A, 2)
A2


# In[41]:


#единичная матрица
I = np.eye(3)
I


# In[42]:


#траспонирование
A = np.array([[ 15,  18,  21],
       [ 42,  54,  66],
       [ 69,  90, 111]])
At = A.T
At


# генерирование массивов

# In[43]:


a = np.zeros ((3, 4))
a


# In[44]:


a = np.ones((5, 3))
a


# In[46]:


np.arange(0,10)
np.arange(0,10, 2)


# In[47]:


np.linspace(0, 9.9, 100)


# In[50]:


np.logspace(0, 3, 2)


# In[53]:


np.reshape(a, (3, -1))


# In[54]:


a = a.flatten() #превращение в олномерный массив
a


# In[59]:


a = np.zeros((2,3))
a
b = np.ones((2,3))
b


# In[60]:


v = np.vstack((a, b)) #соединение матриц
v


# функции для работы с данными

# In[61]:


a = np.random.randint(0, 20, 10)
a


# In[62]:


#индексы, которые удовлетворяют запросу
np.where(a>10)


# In[63]:


a[np.where(a>10)]


# In[ ]:




