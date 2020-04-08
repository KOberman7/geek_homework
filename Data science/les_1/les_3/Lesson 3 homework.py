#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np
from sklearn.datasets import load_boston


# Импортируйте библиотеки pandas и numpy.
# Загрузите "Boston House Prices dataset" из встроенных наборов данных библиотеки sklearn. Создайте датафреймы X и y из этих данных.
# Разбейте эти датафреймы на тренировочные (X_train, y_train) и тестовые (X_test, y_test) с помощью функции train_test_split так, чтобы размер тестовой выборки
# составлял 30% от всех данных, при этом аргумент random_state должен быть равен 42.
# Создайте модель линейной регрессии под названием lr с помощью класса LinearRegression из модуля sklearn.linear_model.
# Обучите модель на тренировочных данных (используйте все признаки) и сделайте предсказание на тестовых.
# Вычислите R2 полученных предказаний с помощью r2_score из модуля sklearn.metrics.

# In[38]:


boston = load_boston()


# In[39]:


data = boston.data
data


# In[40]:


target = boston.target


# In[41]:


feature_names = boston.feature_names
feature_names


# In[42]:


x = pd.DataFrame(data, columns=feature_names)
x


# In[43]:


y = pd.DataFrame(target, columns=['price'])
y


# In[44]:


from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split( x, y, test_size=0.3, random_state=42)


# In[45]:


from sklearn.linear_model import LinearRegression
lr = LinearRegression()


# In[46]:


lr.fit(x_train, y_train)


# In[47]:


y_pred = lr.predict(x_test)


# In[48]:


check_test = pd.DataFrame({'y_test': y_test['price'],
                          'y_pred': y_pred.flatten()},
                         columns=['y_test', 'y_pred'])


# In[49]:


check_test.head(10)


# In[51]:


from sklearn.metrics import r2_score
r2_score1 = r2_score(y_test, y_pred)
r2_score1


# Создайте модель под названием model с помощью RandomForestRegressor из модуля sklearn.ensemble.
# Сделайте агрумент n_estimators равным 1000,
# max_depth должен быть равен 12 и random_state сделайте равным 42.
# Обучите модель на тренировочных данных аналогично тому, как вы обучали модель LinearRegression,
# но при этом в метод fit вместо датафрейма y_train поставьте y_train.values[:, 0],
# чтобы получить из датафрейма одномерный массив Numpy,
# так как для класса RandomForestRegressor в данном методе для аргумента y предпочтительно применение массивов вместо датафрейма.
# Сделайте предсказание на тестовых данных и посчитайте R2. Сравните с результатом из предыдущего задания.
# Напишите в комментариях к коду, какая модель в данном случае работает лучше.
# 

# In[32]:


from sklearn.ensemble import RandomForestRegressor


# In[33]:


model = RandomForestRegressor(n_estimators=1000, max_depth=12, random_state=42)


# In[34]:


model.fit(x_train, y_train.values[:,0])


# In[35]:


y_pred = model.predict(x_test)
y_pred.shape


# In[36]:


check_test = pd.DataFrame({'y_test': y_test['price'],
                          'y_pred': y_pred.flatten()},
                         columns=['y_test', 'y_pred'])
check_test.head(10)


# In[37]:


r2_score2= r2_score(y_test, y_pred)
r2_score2


# In[52]:


r2_score2>r2_score1


# In[53]:


#Вывод: модель RandomForestRegressor работает лучше, чем модель LinearRegression

