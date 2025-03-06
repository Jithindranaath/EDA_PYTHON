import pandas as pd
emp=pd.read_excel(r'c:\Users\ADMIN\Downloads\Rawdata.xlsx')
print(emp)
print(emp.head())
print(emp.tail())
print(emp.info())
print(emp.describe())
print(emp.isnull().sum())
print(emp.shape)
print(emp.columns)
print(emp.dtypes)
print(emp.nunique())
print(emp.count())
print(emp.isnull())
print(id(emp))
print(emp.isna())  #it is a boolean function which prints true if there is Nan in the dataframe
emp['Age']=emp['Age'].str.replace(r'\W','',regex=True) #removes non-word chars from the column
print(emp)
emp['Age']=emp['Age'].str.extract(r'(\d+)') #extract integers from the column
print(emp)
emp['Location']=emp['Location'].str.replace(r'\W','',regex=True)
emp['Domain']=emp['Domain'].str.replace(r'\W','',regex=True)
emp['Name']=emp['Name'].str.replace(r'\W','',regex=True)
print(emp)
emp['Salary']=emp['Salary'].str.extract(r'(\d+)')
emp['Exp']=emp['Exp'].str.extract(r'(\d+)')
print(emp)
Cleaned_data=emp.copy()
print(Cleaned_data)
print(Cleaned_data.isnull().sum())

import numpy as np
Cleaned_data['Age']=Cleaned_data['Age'].fillna(np.mean(pd.to_numeric(Cleaned_data['Age'])))  #as the age is numeric we use mean strategy to fill the missing values(max we use mean strategy only)
print(Cleaned_data['Age'])

Cleaned_data['Exp']=Cleaned_data['Exp'].fillna(np.mean(pd.to_numeric(Cleaned_data['Exp'])))
print(Cleaned_data['Exp'])

Cleaned_data['Location']=Cleaned_data['Location'].fillna(Cleaned_data['Location'].mode()[0])  #it fills the missing values with the most frequent value
print(Cleaned_data['Location'])

print(Cleaned_data.info())

Cleaned_data['Name']=Cleaned_data['Name'].astype('category')
Cleaned_data['Domain']=Cleaned_data['Domain'].astype('category')
Cleaned_data['Location']=Cleaned_data['Location'].astype('category')
print(Cleaned_data.info())

Cleaned_data['Age']=Cleaned_data['Age'].astype('int')
Cleaned_data['Salary']=Cleaned_data['Salary'].astype('int')
Cleaned_data['Exp']=Cleaned_data['Exp'].astype('int')
print(Cleaned_data.info())

Cleaned_data.to_csv('Cleaned_data.csv')
import os
#to get path of the file being stored
print(os.getcwd())

import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')

print(Cleaned_data['Salary'])

vis1=sns.histplot(Cleaned_data['Salary'])
plt.show()

vis2=sns.lmplot(data=Cleaned_data,x='Exp',y='Salary')
plt.show()

vis3=sns.lmplot(data=Cleaned_data,x='Exp',y='Salary',fit_reg=False)
plt.show()

vis4=sns.distplot(Cleaned_data['Salary'])
plt.show()

vis5=sns.histplot(Cleaned_data['Exp'])
plt.show()

vis6=sns.lmplot(data=Cleaned_data,x='Salary',y='Exp',fit_reg=False)
plt.show()

vis7=sns.distplot(Cleaned_data['Age'])
plt.show()

# vis8=sns.distplot(Cleaned_data['Domain'])
# plt.show()

# vis9=sns.distplot(Cleaned_data['Location'])
# plt.show()

# vis10=sns.distplot(Cleaned_data['Name'])
# plt.show()

vis11=sns.lmplot(data=Cleaned_data,x='Age',y='Exp',fit_reg=False)
plt.show()

v=Cleaned_data.drop(['Salary'],axis=1)
print(v)

y=Cleaned_data.drop(['Name','Domain','Age','Location','Exp'],axis=1)
print(y)

imputation=pd.get_dummies(Cleaned_data)
print(imputation)