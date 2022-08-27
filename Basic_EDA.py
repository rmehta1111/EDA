## Initial Analysis ##

#Importing initial libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#Importing heatmap library and pandas-profiling
import calmap
from pandas_profiling import ProfileReport

#Checking initial information
df = pd.read_csv('Insert csv file here.csv')
df.head()
df.info()
# info contains dtypes information but to just see column types information use this
df.dtypes

#If you see some time column type as object here- convert it to datetime64[ns]
# 1/5/19 changes to 2019-01-05
df['Date'] = pd.to_datetime(df['Date'])

#It is convention to set date as index for dataframe
#To do that use set_index command

df.set_index('Date',inplace = True)
#To check this permanent change- use df.head() and see Date as index in place of original 0-indexing

#To check initial summary stats for all numeric columns
df.describe()
#We can use mean of columns from this later for imputation

## Univariate Analysis ##
#Approach should be to pose questions as the datasets vary and do the analysis

#Let's take an example of dataset of a retail chain with 3 store branches having customer sales data and customer ratings
#Some questions might look like-

# Q1) How does the distribution of customer ratings look like and is it skewed?
sns.distplot(df['Rating'])
#This would output a distribution which on inspection might be uniform if a specific value isn't quite high/low
# If you need to see the full output in jupyter and not scroll- select 'Disable scrolling outputs' after right clicking on the cell

#To overlay mean of distribution on the plot
plt.axvline(x=np.mean(df['Rating']),c='red',ls='--')

#To overlay percentile lines-25-75
plt.axvline(x=np.percentile(df['Rating'],25),c='green',ls='--')
plt.axvline(x=np.percentile(df['Rating'],75),c='green',ls='--')

# Q2) Do aggregate sales numbers differ by much between branches?
sns.countplot(df['Branch'])

#To get the count using a method
df['Branch'].value_counts()

#For checking different channels for payments
sns.countplot(df['Payment'])


## Bivariate Analysis ##

# Q3) Is there a relationship between Rating and Gross income?
#We can make a scatterplot between 2 variables to see the distribution of one variable wrt another variable
#x axis parameter comes first
sns.scatterplot(df['Rating'],df['gross income'])

#To check the dependency on the variable we can make a regression plot which will add a regression line on this scatterplot
sns.regplot(df['Rating'],df['gross income'])
#If the line is flat(horizontal), their is no dependency of rating on gross income

#To compare different categories based on another variable(for ex- Ratings dependency on store branch) we can use boxplot
# Is there a relationship between Branch and gross income?
sns.boxplot(x=df['Branch'],y=df['gross income'])
#Here we can compare the line inside the box i.e. median and see if they are closer- In that case, there is no dependency of gross income on Branch

# Is there a relationship between Gender and gross income?
sns.boxplot(x=df['Gender'],y=df['gross income'])
#Can check median and 75th percentile (Upper line to see at 75th percentile do women spend more than men or vice versa)

# Q4) Is there a noticable time trend in gross income?
#We can use lineplot for this
#But here to make a lineplot we need single row for every date
#For that- we roll-up data on the date (index here) using mean of all values on that date using groupby

df.groupby(df.index).mean()

# The index of this grouping and 'gross income' would be used as x and y respectively for the lineplot 
sns.lineplot( x= df.groupby(df.index).mean().index,
              y= df.groupby(df.index).mean()['gross income'])
#The data might be varyng around the same mean- horizontal trend of the wave-
# Some days the gross income might be large and some days low but as such there might not be a time trend for the same- Might differ for longer period of data

#To plot all the bivariate plots- Can be used for small dataset as this is time consuming
sns.pairplot(df)

##  Duplicate rows and missing values ##

#To check how many rows are duplicated
df.duplicated().sum()

#To find duplicate rows
df[df.duplicated()==True]

#To drop duplicate rows- Permanent change in the dataframe itself
df.drop_duplicates(inplace=True)

#To check how many rows have missing values- columnwise
df.isna().sum()

#If we want the proportion of missing values we divide it with the length of dataframe
df.isna().sum()/len(df)

#To visualize these missing values using heatmap
sns.heatmap(df.isnull(),cbar=False)
#Can also use isna() in place of isnull()- cbar False makes it cleaner by removing the heat bar legend

#How to deal with missing values- can use fillna on zeros directly on df.fillna(0)
#Better method would be imputing with mean
df.fillna(df.mean(),inplace=True)

#This will fill all the numeric columns- can check heatmap to verify this
#For categorical columns- we fill them next
df.fillna(df.mode().iloc[0],inplace=True)

#iloc[0] is required as .mode() gives a dataframe with the top row as mode and remaining values
#Can verify filling of all values using heatmap

#For a small dataset- we can use the pandas profiling library to get stats and analysis
dataset = pd.read_csv('Enter csv name.csv')
prof = ProfileReport(dataset)
prof

## Correlation Analysis

#Get correlation between 2 numeric columns
round(np.corrcoef(df['gross income'],df['Rating'])[1][0],2)

#For gettting pairwise correlation between all the numeric columns
np.round(df.corr(),2)

#To visualize and get insights from correlation
sns.heatmap(np.round(df.corr(),2),annot=True)
#Black areas signify that the correlation is not there- this can be used to say a lot with certainity
