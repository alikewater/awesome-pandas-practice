import pandas as pd
import  matplotlib.pyplot as plt

orders = pd.read_excel('Orders.xlsx',index_col='Week')
print(orders)
print(orders.columns)


#折线图，横轴是index列
orders.plot(y=['Accessories', 'Bikes', 'Clothing', 'Components'])
plt.title('Orders Weekly Trend',fontsize=18,fontweight='bold')
plt.ylabel('Total')
plt.xticks(orders.index)


#叠加区域图,横轴是index
orders.plot.area(y=['Accessories', 'Bikes', 'Clothing', 'Components'])
plt.title('Orders Weekly Trend',fontsize=18,fontweight='bold')
plt.ylabel('Total')
plt.xticks(orders.index[orders.index%5==0])#重新铺一遍横坐标

plt.show()