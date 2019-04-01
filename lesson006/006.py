import pandas as pd



books = pd.read_excel('Books.xlsx',index_col='ID')
# print(books.head())

# #以列（Series）的方式实现，所有行的相应列
# books['Price']= books['ListPrice']*books['Discount']#列乘以列，列乘以常数（广播机制）

#以index迭代方式实现,可是先部分行的数据运算
for i in books.index:
    books.at[i,'Price'] = books.at[i,'ListPrice']*books.at[i,'Discount']#采用二维索引
    # books['Price'].at[i] = books['ListPrice'].at[i]*books['Discount'].at[i]#使用Series索引
print(books.head())


#价格添加Price+2
books['Price']=books['Price']+2

print(books.head())

#价格降低Price-2,采用函数apply的方式,函数采用lambda表达式生成
books['Price'] = books['Price'].apply(lambda x:x-2)

print(books.head())