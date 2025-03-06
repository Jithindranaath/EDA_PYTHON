import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os
for dirname,_,filenames in os.walk('/kaggle/input'):
    for filename in filenames:
        print(os.path.join(dirname,filename))
import seaborn as sns
# import spicy.stats as st

df=pd.read_csv(r'c:\Users\ADMIN\Downloads\heart.csv')
print(df.info())
print(df.describe())
print(df.shape)
print(df.head())
print(df.tail())
print(df.columns)

#univariate analysis
print(df['target'].nunique())
print(df['target'].unique())  #here shows the unique values in the target column
print(df['target'].value_counts()) #here shows the count of each unique value in the target column

a=sns.countplot(x='target',data=df,hue='target')
plt.show()

#frequency distribution of target wt sex
print(df.groupby('sex')['target'].value_counts())
#frequency distribution of sex wrt target
b=sns.countplot(x='sex',hue='target',data=df)
plt.show()

b=sns.countplot(x='sex',hue='target',data=df) #(this shows the count of each unique value in the target column)
plt.show()

c=sns.countplot(y='target',hue='sex',data=df)
plt.show()

d=sns.countplot(x='target',data=df,palette='Set3')
plt.show()

e=sns.countplot(x='target',data=df,facecolor=(0,0,0,0),linewidth=5,edgecolor=sns.color_palette('dark',3)) #it makes the bar transparent and make only outer lines visible
plt.show()

f=sns.countplot(x='target',hue='fbs',data=df)
plt.show()
g=sns.countplot(x='target',hue='exang',data=df)
plt.show()

#Bi-variate analysis
correlation=df.corr()
print(correlation['target'].sort_values(ascending=True))

print(df['cp'].nunique())  #prints the number of unique values in the cp column
print(df['cp'].value_counts()) #prints the count of each unique value in the cp column

hehe=sns.countplot(x='cp',data=df,hue='cp')
plt.show()

#frequency of target wrt cp
print(df.groupby('cp')['target'].value_counts())

heh=sns.countplot(x='cp',data=df,hue='target')
plt.show()

ax = sns.catplot(x="target", col="cp", data=df, kind="count", height=8, aspect=1)
plt.show()

he=sns.kdeplot(x='thalach',data=df)
plt.show()

h=sns.kdeplot(x='thalach',data=df,shade=True,color='b')
plt.show()

# e=sns.distplot(x='thalach',kde=False,rug=True,bins=10)
# plt.show()

e=sns.stripplot(x='target',y='thalach',data=df,hue='target')
plt.show()

f=sns.stripplot(x="target", y="thalach", data=df, jitter = 0.01,hue='target') #jitter is used to avoid overplotting
plt.show()

g=sns.boxplot(x='target',y='thalach',data=df,hue='target')
plt.show()

#Multivariate Analysis
