import pandas as pd
movie=pd.read_csv(r'c:\Users\ADMIN\Downloads\Movie-Rating.csv')
print(movie.info())
print(movie.describe())

# df.columns = ["NewName1", "NewName2", "NewName3"]  # Rename all columns
movie.Year=movie.Year.astype('category')
print(movie.info())
print(movie.describe())

from matplotlib import pyplot as plt
import seaborn as sns

sns.set_style('darkgrid')   #for changing the background of the graph
j=sns.jointplot(data=movie,x='Rotten',y='Audience')
plt.show()

j=sns.jointplot(data=movie,x='Rotten',y='Audience',kind='hex')
plt.show()

j=sns.distplot(movie.Audience)
plt.show()

j=sns.distplot(movie.Rotten)
plt.show()

sns.set_style('darkgrid')
plt.show()

j=sns.histplot(movie.Audience,bins=20)
plt.show()

#distribution is divided into several types but these are the most common ones
#the upper graph is uniform distribution(unifrom one has no meaning bcoz they r linear)
#the lower graph is normal distribution(gausian,binomial are other names of normal distribution)
#if mean=median=mode then there is no outliners

j=plt.hist(movie.Budget)
plt.show()

vis=sns.lmplot(data=movie,x='Rotten',y='Audience',fit_reg=True)
plt.show()

vis=sns.lmplot(data=movie,x='Rotten',y='Audience',fit_reg=True,hue='Genre')
plt.show()
#by default matplotlib gives the scale of 0.2 units in graph

# a=sns.heatmap(correlation,square=True,annot=True,fmt='.2f',linecolor='white')
# vis1=sns.boxplot(data=movie,x='Rating',y='Audience',hue='Genre')
# plt.show()

# vis2 = sns.violinplot(data=movie, x='Rating', y='Audience', hue='Genre')
# plt.show()

g=sns.FacetGrid(movie,row='Genre',col='Year',hue='Genre')
g=g.map(plt.scatter,'Rotten','Audience')
plt.show()