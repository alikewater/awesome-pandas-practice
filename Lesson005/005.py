import pandas as pd
from datetime import date,timedelta

def add_month(d,md):
    yd = md//12#添加多少年
    m = d.month+md%12;
    if(m!=12):
        yd = yd + m//12
        m= m%12

    return date(d.year+yd,m,d.day)




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
    #先拿到Series在进行访问
    # books['ID'].at[i]=i+1
    # books['InStore'].at[i] = 'Yes' if i%2==0 else 'No'
    # # books['Date'].at[i] =start+timedelta(days=i) 加添
    # #books['Date'].at[i] =date(start.year+i,start.month,start.day)#加年
    # books['Date'].at[i] = add_month(start,i) #加月

    #直接从DataFrame的角度进行行列访问
    books.at[i,'ID'] = i+1
    books.at[i,'InStore']='Yes' if i%2==0 else 'No'
    books.at[i,'Date'] = add_month(start,i) #加月

books.set_index('ID',inplace=True)

print(books)
books.to_excel('Books_complement.xls')
