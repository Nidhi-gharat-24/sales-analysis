import pandas as pd
pd.set_option('display.max_rows', 50)
pd.set_option('display.max_column',150)
import matplotlib.pyplot as plt

from datetime import datetime as dt
import numpy as np
df = pd.read_excel("Sample - Superstore.xls")
df.head()
df['Quantity'] = df['State']

results = df.groupby('Quantity').sum()
months = [month for month, df in df.groupby('State')]
plt.figure(figsize=(10,5))
plt.plot(months,results['Sales'], color = '#b80045')
plt.xticks(months, rotation='vertical', size = 8)
plt.ylabel('Sales in USD', color='red')
plt.xlabel('State', color='red')
#plt.grid()
plt.show()
