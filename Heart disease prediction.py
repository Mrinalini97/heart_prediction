#!/usr/bin/env python
# coding: utf-8

# In[54]:


import pandas as pd
import sklearn as sk
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pickle

# In[3]:


heart_data = pd.read_csv('heart.csv')


# In[18]:


#for i in heart_data.columns:
#    print(i,"\n",heart_data[i].value_counts(),'\n\n\n')


# In[19]:


#heart_data.shape


# In[21]:


#heart_data.isnull().sum()


# In[22]:


#heart_data.dtypes


# In[29]:


#plt.figure(figsize=(12,12))
#sns.heatmap(data = heart_data.corr(),annot = True)
#plt.show()


# In[35]:


x = heart_data.drop('target',axis = 1 )
y = heart_data['target']


# In[30]:


from sklearn.cross_validation import train_test_split


# In[36]:


x_train, x_test, y_train, y_test  = train_test_split(x,y, random_state =42, test_size = 0.2)


# In[37]:


from sklearn.linear_model import LogisticRegression


# In[38]:


logreg = LogisticRegression()


# In[40]:


logreg.fit(x_train,y_train)


# In[42]:

pickle.dump(logreg,open('model.pkl','wb'))

model = pickle.load(open('model.pkl','rb'))

# In[44]:
print(model.predict([[57,0,1,130,236,0,0,174,0,0,1,1,2]]))
#

# In[ ]:
