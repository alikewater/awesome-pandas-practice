import pandas as pd

products = pd.read_excel('list.xlsx',index_col='ID')

print(products.head())

products.sort_values(by='Price',inplace=True,ascending=True)

print(products)

products.sort_values(by=['Worthy','Price'],inplace=True,ascending=[True,False])

print(products)

