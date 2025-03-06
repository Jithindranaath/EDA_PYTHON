import pandas as pd
df=pd.read_csv(r'c:\Users\ADMIN\Downloads\CountryGDP.csv')
print(df)

print(type(df))
print(df.shape)  #prints no.of row,columns
print(len(df))  #prints no.of rows
print(df.columns)  #prints the values in 1st column
print(df.info())  #prints the overall abstract of the data
print(df.head())  #prints 1st 5 rows as default(if we place a value in it it prints the 1st 'x' rows given)
print(df.tail())  #prints last 5 rows as default(if we place a value in it prints the last 'x' rows given)
print(df[::-1])  #to reverse the data
print(df[:5]) #prints the first 5 rows
print(df[0:200:10]) #prints the rows from start to 200 with step 10
print(df[10:20]) #prints the rows from 10 to 19
print(df.describe) #it gives detailed info abt the data
print(df.describe().transpose())
# df.columns=['A','B','C','D','E']  #it changes the names of 1st row as the list is mutable
# print(df.columns)
print(df['CountryName']) #we can use this for getting only one column
print(df[["CountryName",'CountryCode']]) #for getting 2 or more columns we use double square brackets
print(df.isnull())  #prints true at the missing values
print(df.isnull().sum())  #prints the sum of every column missing values
print(df.dtypes)  #prints the data type of every column
df_categorical=df[['CountryName','CountryCode','IncomeGroup']]  #changing the specific columns into categorical grp
df_numerical=df[['InternetUsers','BirthRate']]  #changing the specific columns into numerical grp
print(df_categorical)
print(df_numerical)
print(df_categorical.describe())
print(df_numerical.describe())

#14/2/2025
print(df[4:8][['CountryName','CountryCode']])  #it prints the rows from 4 to 7 at a specific attribute
df['myCalc']=df.BirthRate * df.InternetUsers  #adding a new column of multiplication of birthrate and internetusers
print(df)
df=df.drop('myCalc',axis=1)
print(df)
print(df.InternetUsers<2)
Filter=df.InternetUsers<2
print(df[Filter])  #to print the countries which are following the condition given in filter
print(len(df[Filter]))
Filter1=df.BirthRate>40
print(df[Filter1])
print(len(df[Filter1]))
print(Filter & Filter1)
print(df[Filter & Filter1])
print(len(df[Filter & Filter1]))
print(df[df.IncomeGroup=='Low income'])
print(df[df.IncomeGroup=='High income'])
print(df.IncomeGroup.unique())
print(df.IncomeGroup.nunique())


import matplotlib.pyplot as plt #visualization
import seaborn as sns #distribution of visualization
plt.rcParams['figure.figsize']=6,2

import warnings
warnings.filterwarnings('ignore')
print(df.InternetUsers)
# vis1=sns.histplot(df['InternetUsers'])
# plt.show()
# vis2=sns.histplot(df['IncomeGroup'])
# plt.show()
# vis3=sns.histplot(df['BirthRate'],bins=10)
# plt.show()
# vis4=sns.boxplot(data=df,x='IncomeGroup',y='BirthRate')
# plt.show()
#outlier is the data points which are very far from other data points
#we can detect outlier by graphs
vis5=sns.lmplot(data=df,x='InternetUsers',y='BirthRate')
plt.show()
vis6=sns.lmplot(data=df,x='InternetUsers',y='BirthRate',fit_reg=False)
plt.show()

# kaggle.com-dataset+code
# uci.com-only dataset
# huggingface-dataset and code for llm

rating=pd.read_csv(r'c:\Users\ADMIN\Downloads\archive\rating.csv')
print(rating.shape)