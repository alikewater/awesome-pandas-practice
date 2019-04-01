import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

pd.options.display.max_columns = 999
orders = pd.read_excel('Orders.xlsx')
print(orders.Date.dtype)

orders['Year'] = pd.DatetimeIndex(orders['Date']).year;#转化某列为时间索引类型
print(orders.head(3))

#使用pandas 的api制作
pv1 = orders.pivot_table(index='Category',columns='Year',values='Total',aggfunc=np.sum)
print(pv1)

#使用groupby方式自定义制作
groups = orders.groupby(['Category','Year'])
s = groups['Total'].sum()
c = groups['ID'].count()
pv2 = pd.DataFrame({'Sum':s,'Count':c})
print(pv2)

