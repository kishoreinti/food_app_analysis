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

#graph analysis   - 7

pivot_table=dataframe.pivot_table(index="listed_in(type)",columns='online_order',aggfunc='size',fill_value=0)
sb.heatmap(pivot_table,annot=True,cmap="YlGnBu",fmt='d')
plt.title("heatmap")
plt.xlabel("online order")
plt.ylabel("listed in (type)")
plt.show()

