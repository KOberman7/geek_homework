#!/usr/bin/env python
# coding: utf-8

# Импортируйте библиотеки pandas, numpy и matplotlib.
# Загрузите "Boston House Prices dataset" из встроенных наборов данных библиотеки sklearn.
# Создайте датафреймы X и y из этих данных.
# Разбейте эти датафреймы на тренировочные (X_train, y_train) и тестовые (X_test, y_test)
# с помощью функции train_test_split так, чтобы размер тестовой выборки
# составлял 20% от всех данных, при этом аргумент random_state должен быть равен 42.
# Масштабируйте данные с помощью StandardScaler.
# Постройте модель TSNE на тренировочный данных с параметрами:
# n_components=2, learning_rate=250, random_state=42.
# Постройте диаграмму рассеяния на этих данных.
# 

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# In[2]:


from sklearn.datasets import load_boston


# In[5]:


boston = load_boston()


# In[7]:


data = boston.data
target = boston.target
feature_names = boston.feature_names
x = pd.DataFrame(data, columns=feature_names)
y = pd.DataFrame(target, columns=['price'])


# In[8]:


from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split( x, y, test_size=0.2, random_state=42)


# In[9]:


from sklearn.preprocessing import StandardScaler


# In[10]:


scaler = StandardScaler()


# In[11]:


x_train_scaled = scaler.fit_transform(x_train)
x_test_scaled = scaler.transform(x_test)


# In[12]:


x_train_scaled = pd.DataFrame(x_train_scaled, columns=feature_names)
x_test_scaled = pd.DataFrame(x_test_scaled, columns=feature_names)


# In[13]:


from sklearn.manifold import TSNE
tsne = TSNE(n_components=2, learning_rate=250, random_state=42)
x_train_tsne = tsne.fit_transform(x_train_scaled)


# In[14]:


plt.scatter(x_train_tsne[:,0], x_train_tsne[:,1])


# С помощью KMeans разбейте данные из тренировочного набора на 3 кластера,
# используйте все признаки из датафрейма X_train.
# Параметр max_iter должен быть равен 100, random_state сделайте равным 42.
# Постройте еще раз диаграмму рассеяния на данных, полученных с помощью TSNE,
# и раскрасьте точки из разных кластеров разными цветами.
# Вычислите средние значения price и CRIM в разных кластерах.
# 

# In[15]:


from sklearn.cluster import KMeans


# In[17]:


kmeans = KMeans(n_clusters=3, max_iter=100, random_state=42)


# In[19]:


labels_train = kmeans.fit_predict(x_train_scaled)
plt.scatter(x_train_tsne[:, 0], x_train_tsne[:, 1], c=labels_train)
plt.show()


# In[21]:


print('Средние значения price:')
print('Кластер 0: {}'.format(y_train[labels_train == 0].mean()))
print('Кластер 1: {}'.format(y_train[labels_train == 1].mean()))
print('Кластер 2: {}'.format(y_train[labels_train == 2].mean()))
print('Средние значения CRIM:')
print('Кластер 0: {}'.format(x_train.loc[labels_train == 0, 'CRIM'].mean()))
print('Кластер 1: {}'.format(x_train.loc[labels_train == 1, 'CRIM'].mean()))
print('Кластер 2: {}'.format(x_train.loc[labels_train == 2, 'CRIM'].mean()))

