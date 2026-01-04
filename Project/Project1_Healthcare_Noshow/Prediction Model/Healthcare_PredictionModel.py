#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd

df = pd.read_csv("healthcare_dataset_cleaned.csv")
df.head()


# In[2]:


features = [
    "age",
    "gender",
    "appointment_month",
    "appointment_year",
    "appointment_shift",
    "under_12_years_old",
    "over_60_years_old",
    "patient_needs_companion",
    "average_temp_day",
    "rain_intensity",
    "heat_intensity"
]

target = "no_show"


# In[7]:


df["gender"].unique()


# In[8]:


df["gender"] = df["gender"].map({"M": 0, "F": 1})


# In[9]:


df["gender"].unique()


# In[13]:


df["appointment_month"] = pd.to_datetime(
    df["appointment_month"],
    format="%B",
    errors="coerce"
).dt.month


# In[14]:


df["appointment_month"].unique()


# In[16]:


df["appointment_shift"].unique()


# In[17]:


df["appointment_shift"] = df["appointment_shift"].map({
    "Morning": 0,
    "Afternoon": 1,
    "Evening": 2
})


# In[18]:


df["rain_intensity"].unique()


# In[19]:


df["rain_intensity"] = df["rain_intensity"].map({
    "weak": 0,
    "moderate": 1,
    "heavy": 2
})


# In[20]:


df["heat_intensity"].unique()


# In[21]:


df["heat_intensity"] = df["heat_intensity"].map({
    "mild": 0,
    "cold": 1,
    "warm": 2
})


# In[22]:


X = df[features]
print(X.dtypes)


# In[23]:


X = df[features]
y = df[target]


# In[24]:


from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42
)


# In[25]:


from sklearn.tree import DecisionTreeClassifier

model = DecisionTreeClassifier(
    max_depth=5,
    random_state=42
)

model.fit(X_train, y_train)


# In[30]:


from sklearn.metrics import accuracy_score

accuracy = accuracy_score(y_test, y_pred)
accuracy


# In[ ]:


import pandas as pd

# Create feature importance dataframe
importance = pd.Series(
    model.feature_importances_,
    index=features
).sort_values(ascending=False)

# Display feature importance
importance


# In[ ]:


importance.to_csv("feature_importance.csv")

