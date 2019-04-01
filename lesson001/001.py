import pandas as pd;
import numpy as np;

#通过两个dict直接构造，dict的每个键值对为列名和列值
# df = pd.DataFrame({'ID': [1,2,3],"Number":['Tim','Victor','Lim']})

#从 list构造
#
list = [[1,'Tim'],[2,'Victor'],[3,'Lim']]
# df = pd.DataFrame(list,columns=['ID','Number'])


#从numpy array 构造
array = np.array(list)
# print(array)
df = pd.DataFrame(array,columns=['ID','Number'])
print(df.columns)


df=df.set_index('ID')

#dataframe转化为array
print(df)

foo = df.values

print(foo)

foo = np.array(df)
print(foo)
# df.to_excel('001.xls');
# print('Done')

