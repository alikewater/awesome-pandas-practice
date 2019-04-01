import pandas as pd
import matplotlib.pyplot as plt


pd.options.display.max_columns=777
homes = pd.read_excel('home_data.xlsx')
print(homes.columns)
# ['id', 'price', 'bedrooms', 'bathrooms', 'sqft_living', 'sqft_basement',
#        'sqft_lot', 'floors', 'yr_built']

#散点图绘制
# homes.plot.scatter(x='sqft_living',y='price')


print('居住面积绘制直方图')
#绘制直方图(频度图)
homes.sqft_living.plot.hist(bins=100)
plt.xticks(range(0,max(homes.sqft_living),500),fontsize=8,rotation=90)
plt.show()

print('价格直方图')
homes.price.plot.hist(bins=100)
plt.xticks(range(0,max(homes.price),1000000),fontsize=8,rotation=90)
plt.show()

print('相关性检测')

print(homes.corr())
