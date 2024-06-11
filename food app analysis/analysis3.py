import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb

dataframe=pd.read_csv("fooddata.csv")

def handleRate(value):
     value=str(value).split('/')
     value=value[0];
     return float(value)

dataframe['rate']=dataframe['rate'].apply(handleRate)
pd.options.display.max_rows=9999
#graph analysis   - 3

max_votes=dataframe['votes'].max()
restaurant_with_max_votes=dataframe.loc[dataframe['votes']==max_votes,'name']
sb.countplot(x=dataframe['online_order'])
plt.show()

