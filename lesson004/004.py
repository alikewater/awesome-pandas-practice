import pandas as pd
from datetime import date,timedelta

#跳过空行读取,指定使用的列,指定索引列，没有为None
books = pd.read_excel('Books.xlsx',skiprows=3,usecols='C:F',index_col=None,
                      dtype={'ID':str,'InStore':str,'Date':str})
# print(books)
#数据中为空的部分，读取后填充为NaN,数据类型为float64
#通过中括号和列标引用列,每个列是一个Series，通过at访问Series的元素，可读可写
books['ID'].at[0]=100
print(books['ID'])
start = date(2018,1,1)

for i in books.index:
    books['ID'].at[i]=i+1
    books['InStore'].at[i] = 'Yes' if i%2==0 else 'No'
    books['Date'].at[i] =start

print(books)