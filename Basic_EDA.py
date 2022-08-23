import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#Importing heatmap library
import calmap
from pandas_profiling import ProfileReport

df = pd.read_csv('Insert csv file here'.csv)
df.head()
df.info()

#If you see some time column type as object here- convert it to datetime
df['Date'] = pd.to_datetime(df['Date'])
