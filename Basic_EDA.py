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

# Q2) Do aggregate sales numbers differ by much between branches?


