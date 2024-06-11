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
#graph analysis   - 6

plt.figure(figsize=(6,6))
sb.boxplot(x="online_order",y="rate",data=dataframe)
plt.show()
