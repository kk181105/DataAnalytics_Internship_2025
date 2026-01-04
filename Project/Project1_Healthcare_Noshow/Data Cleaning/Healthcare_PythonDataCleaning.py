#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np


# In[4]:


import os
os.getcwd()


# In[5]:


os.listdir()


# In[6]:


df=pd.read_csv("healthcare_dataset.csv")
df.head()


# In[7]:


df.info()


# In[9]:


df.rename(columns={"No-show": "NoShow"}, inplace=True)


# In[17]:


for col in df.columns:
    print(col)


# In[22]:


df.columns = df.columns.str.strip().str.lower()


# In[25]:


df["appointment_date"] = pd.to_datetime(
    df["appointment_date"],
    dayfirst=True
)


# In[26]:


df["appointment_date"] = pd.to_datetime(
    df["appointment_date"],
    dayfirst=True,
    errors="coerce"
)


# In[28]:


df = df.dropna(subset=["appointment_date"])


# In[29]:


df["appointment_weekday"] = df["appointment_date"].dt.day_name()


# In[30]:


df["appointment_date"].head()
df["appointment_weekday"].value_counts()


# In[31]:


df["appointment_date"] = pd.to_datetime(
    df["appointment_date"],
    dayfirst=True,
    errors="coerce"
)


# In[33]:


df["appointment_weekday"] = df["appointment_date"].dt.day_name()


# In[34]:


df["no_show"] = df["no_show"].map({"Yes": 1, "No": 0})


# In[35]:


df["gender"] = df["gender"].map({"M": 0, "F": 1})


# In[36]:


df = df[df["age"] >= 0]


# In[37]:


df.drop(columns=[
    "specialty",
    "appointment_time",
    "no_show_reason",
    "date_of_birth",
    "entry_service_date",
    "city",
    "icd"
], inplace=True)


# In[38]:


df.head()
df.isnull().sum()


# In[47]:


df = df.dropna(subset=["no_show"])


# In[48]:


df["average_temp_day"] = df["average_temp_day"].fillna(df["average_temp_day"].median())
df["rain_intensity"] = df["rain_intensity"].fillna(0)
df["heat_intensity"] = df["heat_intensity"].fillna(0)


# In[49]:


df.to_csv("healthcare_dataset_cleaned.csv", index=False)


# In[ ]:




