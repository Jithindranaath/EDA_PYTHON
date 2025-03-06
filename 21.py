import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

#Load Titanic dataset
@st.cache
def load_data():
    data=pd.read_csv(r'c:\Users\ADMIN\Downloads\titanic dataset.csv')
    return data

data=load_data()

st.title('EDA of titanic dataset')
st.write('this is an eda on the titanic dataset')
st.write('first few rows of the dataset')
st.dataframe(data.head())

st.subheader('Missing values')
missing_data=data.isnull().sum()
st.write(missing_data)

if st.checkbox('Fill missing Age with median'):
    data['Age'].fillna(data['Age'].median(), inplace=True)

if st.checkbox('Fill missing Embarked with mode'):
    data['Embarked'].fillna(data['Embarked'].mode()[0], inplace=True)

if st.checkbox('Drop duplicates'):
    data.drop_duplicates(inplace=True)

st.subheader('Cleaned Dataset')
st.dataframe(data.head())

# EDA Section
st.subheader('Statistical Summary of the Data')
st.write(data.describe())  #we use describe for statistical info abt the dataset

# Age Distribution
st.subheader('Age Distribution')
fig, ax = plt.subplots()
sns.histplot(data['Age'], kde=True, ax=ax)
ax.set_title('Age Distribution')
st.pyplot(fig)

# Gender Distribution
st.subheader('Gender Distribution')
fig, ax = plt.subplots()
sns.countplot(x='Sex', data=data, ax=ax)
ax.set_title('Gender Distribution')
st.pyplot(fig)

# Pclass vs Survived
st.subheader('Pclass vs Survived')
fig, ax = plt.subplots()
sns.countplot(x='Pclass', hue='Survived', data=data, ax=ax)
ax.set_title('Pclass vs Survived')
st.pyplot(fig)

'''
# Correlation Heatmap
st.subheader('Correlation Heatmap')
fig, ax = plt.subplots()
sns.heatmap(data.corr(), annot=True, cmap='coolwarm', ax=ax)
ax.set_title('Correlation Heatmap')
st.pyplot(fig)
'''

# Feature Engineering Section
st.subheader('Feature Engineering: Family Size')
data['FamilySize'] = data['SibSp'] + data['Parch']
fig, ax = plt.subplots()
sns.histplot(data['FamilySize'], kde=True, ax=ax)
ax.set_title('Family Size Distribution')
st.pyplot(fig)

# Conclusion Section
st.subheader('Key Insights')
insights = """
- Females have a higher survival rate than males.
- Passengers in 1st class had the highest survival rate.
- The majority of passengers are in Pclass 3.
- Younger passengers tended to survive more often.
"""
st.write(insights)