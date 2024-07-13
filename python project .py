#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import seaborn as sns


# In[2]:


df = pd.read_csv ('Diwali Sales Data.csv', encoding= 'unicode_escape')


# In[3]:


df.shape


# In[4]:


df.head()


# In[5]:


df.info()


# In[6]:


df.drop(['Status','unnamed1'], axis=1, inplace=True)


# In[7]:


df


# In[8]:


pd.isnull(df).sum()


# In[9]:


df.dropna(inplace =True)


# In[10]:


df.shape


# In[11]:


df.describe()


# # Exploratory data analysis

# # GENDER

# In[12]:


ax = sns.countplot (data = df, x ='Gender' )

for bars in ax.containers: 
    ax.bar_label(bars)


# Gender v/s Total Amount 

# In[17]:


gen_sales = df.groupby(['Gender'], as_index = False)['Amount'].sum().sort_values(by ='Amount' ,ascending = False) 
sns.barplot (x= 'Gender',y='Amount',data = gen_sales)


# from this we can see most of the buyers are female 

# # AGE 

# In[36]:


ax = sns.countplot ( x= 'Age Group', hue = 'Gender',data = df)

for bars in ax.containers:
        ax.bar_label(bars)
    


# TOTAL AMOUNT V/S AGE GROUP 

# In[37]:


age_group = df.groupby (['Age Group'],as_index = False)['Amount'].sum().sort_values(by ='Amount', ascending = False)
sns.barplot (x= 'Age Group',y='Amount',data = age_group)


# here most buyers are from the age group of 26-35

# # state 

# In[40]:


df.head()


# In[51]:


st_state = df.groupby(['State'], as_index =False)['Orders'].sum().sort_values(by='Orders',ascending = False).head(10)
sns.set(rc={'figure.figsize':(15,6)})
sns.barplot (data= st_state ,x = 'State', y ='Orders')


# In[52]:


st_state = df.groupby(['State'], as_index =False)['Amount'].sum().sort_values(by='Amount',ascending = False).head(10)
sns.set(rc={'figure.figsize':(15,6)})
sns.barplot (data= st_state ,x = 'State', y ='Amount')


# here we see that most of the orders and total amount are from  uttarpradhesh ,maharashtra and karnataka 

# # Martial status 

# In[53]:


df.head()


# In[63]:


status_m = df.groupby(['Marital_Status','Gender'], as_index = False)['Amount'].sum().sort_values(by='Amount',ascending=False)
sns.set(rc={'figure.figsize':(5,3)})
sns.barplot(data = status_m, x='Marital_Status', y= 'Amount', hue = 'Gender' )


# here we see that married female are most of the buyers 

# # occupation 

# In[64]:


df.head()


# In[65]:


sales_occup = df.groupby(['Occupation'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)

sns.set(rc={'figure.figsize':(15,5)})
sns.barplot(data = sales_occup, x = 'Occupation',y= 'Amount')


# here mosat of the buyers are from IT,healthcare,aviation sector 

# # product category

# In[67]:


df.head()


# In[70]:


sales_prod = df.groupby(['Product_Category'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False).head(10)

sns.set(rc={'figure.figsize':(20,5)})
sns.barplot(data = sales_prod, x = 'Product_Category',y= 'Amount')


# here most buying products are food , clothing and electronic gadgets 

# # conclusion 

# Married women age group 26-35 yrs from UP,  Maharastra and Karnataka working in IT, Healthcare and Aviation are more likely to buy products from Food, Clothing and Electronics category

# In[ ]:




