import pandas as pd;

#读取数据
df = pd.read_excel('People.xlsx')


#查看数据形态
print(df.shape)
print((df.columns))
print(df.head())
print('======================')
print(df.tail(3))


print('读取脏文件头')
#读取文件头错位的文件(制定head)，表明从哪里开始读取
#文件投在第二行
people=pd.read_excel('People01.xlsx',header=1,index_col='ID')

print(people.columns)
people.set_index('ID',inplace=True)
print(people.head(3))

#忽略文件头，读取后自动生成文件头
print('===========忽略文件头，读取后自动生成文件头============')
people=pd.read_excel('People.xlsx')
print(people.columns)#Int64Index([0, 1, 2, 3, 4, 5], dtype='int64')
print('制定文件列：')
people.columns = ['ID', 'Type', 'Title', 'FirstName', 'MiddleName', 'LastName']

print(people.columns)


print('==============写入文件，指定index=================')
people = people.set_index('ID')#直接用设置了index的新的dataframe替换原来的datarame

print(people.head(2))

people.to_excel('output.xls')

print('==============读取文件，指定index=================')
people = pd.read_excel('output.xls',index_col='ID')

print(people.head(3))

