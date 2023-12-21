#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


df = pd.read_csv(r"C:\Users\Lenovo\Downloads\dailyActivity_merged.csv")
df


# In[3]:


df.info()


# In[25]:


df[df['Calories']==df['Calories'].min()]


# In[29]:


#most inactive days are 5/12/2016,5/10/2016,4/30/2016


# In[30]:


df[df['Calories']==df['Calories'].max()]


# In[31]:


#most active day is 4/21/2016


# In[88]:


import plotly.express as px


# In[92]:


px.scatter(df,x='ActivityDate',y='Calories',title='Calries Burned')


# In[93]:


# graph of active and inactive day based on calories


# In[87]:


px.scatter(df,x='ActivityDate',y='Calories',color='TotalSteps',hover_data=['Id'])


# In[ ]:


#Based on the scatter plot, it appears that individual with ID 8877689391 has the highest ratio of total steps to calories burned


# In[63]:


above_average_total_steps=df[df['TotalSteps']>df['TotalSteps'].mean()]


# In[69]:


above_average_total_steps['ActivityDate'].unique()


# In[59]:


#These are the above average active days based on total steps


# In[60]:


below_average_total_steps=df[df['TotalSteps']<df['TotalSteps'].mean()]


# In[70]:


below_average_total_steps['ActivityDate'].unique()


# In[71]:


#these are below average active days based on total steps


# In[ ]:




