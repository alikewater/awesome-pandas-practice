import pandas as pd
import matplotlib.pyplot as plt

pd.options.display.max_columns =777
homes =pd.read_excel('home_data.xlsx')
print(homes.head())
print(homes.describe())

homes.sqft_living.plot.kde()
plt.xticks(range(min(homes.sqft_living),max(homes.sqft_living),1000),rotation=90)
plt.show()
