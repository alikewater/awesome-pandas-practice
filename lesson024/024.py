import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

sales = pd.read_excel('Sales.xlsx',dtype={'Month':str})
print(sales.head(3))
# print(sales.Month)
sales['Month'] = sales['Month'].astype("str")
xts = sales.Month.astype("str")
print(xts)

#采用线性回归进行曲线拟合

slope,intercept,r,p,std_err = linregress(sales.index,sales.Revenue)

exp = sales.index*slope + intercept

# plt.bar(sales.index,sales.Revenue)
plt.scatter(sales.index,sales.Revenue)
plt.plot(sales.index,exp,color='orange')
plt.title("Sales y= %f *x+ %f" % (slope,intercept))
# plt.xticks(xts,rotation=90)
plt.tight_layout()
plt.show()