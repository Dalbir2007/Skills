#!/usr/bin/env python
# coding: utf-8

# In[5]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
gas = pd.read_csv('vehicles1.csv')
print(gas.head())


# In[6]:


gas.info()


# In[25]:


print(gas.replace(r'', np.nan, regex=True))


# In[38]:


gas['cylinders'].fillna(0, inplace=True)
gas['drive'].fillna(0, inplace=True)
gas['displ'].fillna(0, inplace=True)
gas['eng_dscr'].fillna(0, inplace=True)
gas['trany'].fillna(0, inplace=True)
gas['guzzler'].fillna(0, inplace=True)
gas['trans_dscr'].fillna(0, inplace=True)
gas['tCharger'].fillna(0, inplace=True)
gas['sCharger'].fillna(0, inplace=True)
gas['atvType'].fillna(0, inplace=True)
gas['fuelType2'].fillna(0, inplace=True)
gas['rangeA'].fillna(0, inplace=True)
gas['evMotor'].fillna(0, inplace=True)
gas['startStop'].fillna(0, inplace=True)


# In[39]:


print(gas.isnull().sum())


# In[28]:


gas.sort_values(by='year', ascending=False)


# In[59]:


print(gas['make'].value_counts())


# In[62]:


print(gas['year'].value_counts())


# In[33]:


import matplotlib.pyplot as plt
fig, ax = plt.subplots()
ax.scatter(gas['year'], gas['comb08'])
plt.xlabel('Years')
plt.ylabel('Gas Mileage')
plt.title('Combined Mileage of Cars')
plt.show()


# In[34]:



fig, ax = plt.subplots()
ax.scatter(gas['year'], gas['city08'])
plt.xlabel('Years')
plt.ylabel('Gas Mileage')
plt.title('InCity Mileage of Cars')
plt.show()


# In[37]:


fig, ax = plt.subplots()
ax.scatter(gas['year'], gas['highway08'])
plt.xlabel('Years')
plt.ylabel('Gas Mileage')
plt.title('Highway Mileage of Cars')
plt.show()


# In[ ]:





# In[ ]:




