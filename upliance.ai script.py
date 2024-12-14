#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd

# Using the full path to the Excel file
file_path = r"C:\Users\user\Downloads\Assignment.xlsx"

# Loading the specific sheet
order_details = pd.read_excel(file_path, sheet_name="OrderDetails.csv")

# Checking the first few rows to confirm
print(order_details.head())


# In[5]:


# Calculating the mean of the Rating column, ignoring NaN values
mean_rating = order_details['Rating'].mean()

# Filling missing Rating values with the mean
order_details['Rating'].fillna(mean_rating, inplace=True)

# Verifying if all missing values are handled
print(order_details.isnull().sum())



# In[6]:


# Loading other datasets
user_details = pd.read_excel(file_path, sheet_name="UserDetails.csv")
cooking_sessions = pd.read_excel(file_path, sheet_name="CookingSessions.csv")

# Merging UserDetails with OrderDetails on 'User ID'
merged_data = pd.merge(order_details, user_details, on="User ID", how="inner")

# Merging the result with CookingSessions on 'Session ID'
final_data = pd.merge(merged_data, cooking_sessions, on="Session ID", how="inner")

# Checking the structure of the final merged dataset
print(final_data.head())


# In[7]:


# Correlation between Session Rating and Order Rating
correlation = final_data['Session Rating'].corr(final_data['Rating'])
print(f"Correlation between Session Rating and Order Rating: {correlation}")


# In[8]:


# Counting frequency of dishes
popular_dishes = final_data['Dish Name_x'].value_counts()
print("Popular Dishes:\n", popular_dishes)


# In[9]:


# Average rating by location
avg_rating_location = final_data.groupby('Location')['Rating'].mean()
print("Average Rating by Location:\n", avg_rating_location)

# Total orders by age group
final_data['Age Group'] = pd.cut(final_data['Age'], bins=[0, 20, 30, 40, 50], labels=['<20', '20-30', '30-40', '40-50'])
orders_by_age = final_data.groupby('Age Group')['Order ID'].count()
print("Total Orders by Age Group:\n", orders_by_age)


# In[10]:


import seaborn as sns
import matplotlib.pyplot as plt

# Ploting heatmap for correlation
plt.figure(figsize=(6, 4))
sns.heatmap([[final_data['Session Rating'].corr(final_data['Rating'])]], annot=True, cmap="coolwarm", cbar=True, 
             xticklabels=["Session Rating"], yticklabels=["Order Rating"])
plt.title("Correlation between Session Rating and Order Rating")
plt.show()


# In[11]:


popular_dishes = final_data['Dish Name_x'].value_counts()
plt.figure(figsize=(8, 6))
popular_dishes.plot(kind='bar', color='skyblue', edgecolor='black')
plt.title("Popular Dishes")
plt.xlabel("Dish Name")
plt.ylabel("Number of Orders")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.show()


# In[12]:


avg_rating_location = final_data.groupby('Location')['Rating'].mean()
plt.figure(figsize=(8, 6))
avg_rating_location.plot(kind='bar', color='lightcoral', edgecolor='black')
plt.title("Average Rating by Location")
plt.xlabel("Location")
plt.ylabel("Average Rating")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.show()


# In[13]:


final_data['Age Group'] = pd.cut(final_data['Age'], bins=[0, 20, 30, 40, 50], labels=['<20', '20-30', '30-40', '40-50'])
orders_by_age = final_data.groupby('Age Group')['Order ID'].count()
plt.figure(figsize=(8, 6))
orders_by_age.plot(kind='bar', color='lightgreen', edgecolor='black')
plt.title("Total Orders by Age Group")
plt.xlabel("Age Group")
plt.ylabel("Total Orders")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()


# In[ ]:




