#!/usr/bin/env python
# coding: utf-8

# #  Importing Libraries

# In[1]:


import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt     
get_ipython().run_line_magic('matplotlib', 'inline')
import seaborn as sns
sns.set()
import warnings
warnings.filterwarnings('ignore')


# # Loading the Dataset

# In[2]:


df = pd.read_csv("Diwali Sales Data (1).csv",encoding= 'unicode_escape')


# In[3]:


df.shape


# In[4]:


df


# In[5]:


df.info()


# In[6]:


for col in df.columns:
    print(col)
    print(df[col].unique())


# In[7]:


#drop unrelated/blank columns
df.drop(['Status', 'unnamed1'], axis=1, inplace=True)


# In[8]:


df.isna().sum()


# In[9]:


## Drop null values
df.dropna(inplace = True)


# In[10]:


df.info()


# In[11]:


# change data type
df['Amount'] = df['Amount'].astype('int')


# In[12]:


df.columns


# In[13]:


df.describe()


# In[14]:


df.describe(include = 'object')


# # Exploratory Data Analysis
# 
# ### Gender

# In[15]:


### plotting a bar chart for Gender and it's count

ax = sns.countplot(x = 'Gender',data = df)

for bars in ax.containers:
    ax.bar_label(bars)
plt.show()


# In[16]:


#### plotting a bar chart for gender vs total amount

sales_gen = df.groupby(['Gender'],as_index = False)['Amount'].sum().sort_values(by = 'Amount' ,ascending = False)

ax = sns.barplot(x = 'Gender',y= 'Amount',data = sales_gen, palette = 'Set2')
plt.show()


# From above graphs we can see that most of the buyers are females and even the purchasing power of females are greater than men

# # Age

# In[17]:


ax = sns.countplot(data = df ,x = 'Age Group', hue = 'Gender')

for bars in ax.containers:
  ax.bar_label(bars)


# In[18]:


# Total Amount vs Age Group

sales_age = df.groupby(['Age Group'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)

sns.barplot(x = 'Age Group',y= 'Amount' ,data = sales_age)


# From above graphs we can see that most of the buyers are of age group between 26-35 yrs female

# #  State

# In[19]:


# total number of orders from top 10 states

sales_state = df.groupby(['State'] , as_index = False)['Orders'].sum().sort_values(by = 'Orders' , ascending = False).head(10)

plt.figure(figsize = (20,5))
sns.barplot(x = 'State' , y= 'Orders' , data = sales_state )


# In[20]:


# total amount/sales from top 10 states

sales_state = df.groupby(['State'] , as_index = False)['Orders'].sum().sort_values(by = 'Orders' , ascending = False).head(10)

plt.figure(figsize = (20,5))
sns.barplot(x = 'State' , y= 'Orders' , data = sales_state )

for index,value in enumerate(sales_state['Orders']):
  plt.text(index, value+1.5, str(value), ha = 'center')


# From above graphs we can see that most of the orders & total sales/amount are from Uttar Pradesh, Maharashtra and Karnataka respectively

# # Marital Status

# In[21]:


ax = sns.countplot(data = df, x = 'Marital_Status')

plt.plot(figsize = (7 , 5))

for bars in ax.containers:
  ax.bar_label(bars)


# In[22]:


sales_state = df.groupby(['Marital_Status','Gender'] , as_index = False)['Amount'].sum().sort_values(by = 'Amount', ascending = False)

plt.figure(figsize = (6,5))
sns.barplot(data = sales_state , x = 'Marital_Status' , y = 'Amount' , hue = 'Gender')


# From above graphs we can see that most of the buyers are married (women) and they have high purchasing power

# # Occupation

# In[23]:


plt.figure(figsize = (20,5))

ax = sns.countplot(data = df , x = 'Occupation')

for bars in ax.containers:
  ax.bar_label(bars)


# In[24]:


sales_state = df.groupby(['Occupation'] , as_index = False)['Amount'].sum().sort_values(by = 'Amount' , ascending = False)

plt.figure(figsize = (22,5))
sns.barplot(data = sales_state , x = 'Occupation' , y = 'Amount')


# From above graphs we can see that most of the buyers are working in IT, Healthcare and Aviation sector

# # Product Category

# In[25]:


plt.figure(figsize = (30,10))

ax = sns.countplot(data = df , x = 'Product_Category')

for bars in ax.containers:
  ax.bar_label(bars)


# In[26]:


sales_state = df.groupby(['Product_Category'],as_index = False)['Amount'].sum().sort_values(by = 'Amount' , ascending = False).head(10)

plt.figure(figsize = (25,5))
sns.barplot(data = sales_state , x='Product_Category', y = 'Amount')


# From above graphs we can see that most of the sold products are from Food, Clothing and Electronics category

# # Most saled product

# In[27]:


sales_state = df.groupby(['Product_ID'], as_index = False)['Orders'].sum().sort_values('Orders',ascending = False).head(10)

plt.figure(figsize = (20,5))
sns.barplot(data = sales_state , x = 'Product_ID' , y = 'Orders')


# #  Conclusion

# Married women age group 26-35 yrs from UP, Maharastra and Karnataka working in IT, Healthcare and Aviation are more likely to buy products from Food, Clothing and Electronics category
