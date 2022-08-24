
#Importing libraries
import plotly.express as px
import pandas as pd
import numpy as np

#How to get cancer dataset from sklearn?

#Here reading from pre-shared csv
cancer_df = pd.read_csv('cancer.csv')
cancer_df.head()

#tail can be used to check the number of datapoints in the dataframe
cancer_df.tail()

## Boxplots ##
#To plot a boxplot you can use
sns.boxplot(x=df['target'],y=df['mean area'])
#Boxplot can be used to find outliers

#Equivalent of this in plotly express is
fig = px.box(cancer_df,x='target',y='mean area')
fig.show()

#To see all the points in the boxplot itself
fig = px.box(cancer_df,x='target',y='mean area',points='all')
fig.show()

## Histogram ##
#How to get nbins for histogram?
fig = px.histogram(cancer_df,x='mean radius',nbins=60)
fig.show()

#To add a target parameter also to the histogram
fig = px.histogram(cancer_df,x='mean radius',color='target',nbins=60)
fig.show()
#Very powerful to get initial insights for the target variable

#Histogram plots with marginal plots

#Marginal plot of type 'rug'
px.histogram(cancer_df,x='mean radius',color='target',marginal='rug',nbins=60).show()

#Marginal plot of type 'box'- Can check Q1,Q3, upper fence and lower fence for the target variables
px.histogram(cancer_df,x='mean radius',color='target',marginal='box',nbins=60).show()

#Marginal plot of type 'violin'- Can check Q1,Q3, upper fence and lower fence for the target variables
px.histogram(cancer_df,x='mean radius',color='target',marginal='violin',nbins=60).show()

## Interactive Density HeatMap
#It is a 2D visualization of a histogram
px.density_heatmap(cancer_df,x='mean radius',y='mean texture')

## Scatter-plot matrix ##
px.scatter_matrix(university_df,height=1200,width=1200)

#To make scatter matrix for selected columns in a dataset- add dimensions parameter
px.scatter_matrix(cancer_df,dimensions=['mean texture','mean radius','mean perimeter'])

#To add color to this scatter matrix for selected columns in a dataset- add color parameter as before
px.scatter_matrix(cancer_df,dimensions=['mean texture','mean radius','mean perimeter'],color='target')

## Interactive violin plot ##
