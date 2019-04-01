import pandas as pd

#dict创建Series
d={'x':100,'y':200,'z':300}
s1= pd.Series(d)

print(s1.index )


#通过list创建Series
L1=['x','y','z'];
L2=[100,200,300];

s2 = pd.Series(L2,index=L1)
print(s2)

#序列可以作为一行也可以作为一列

s1 = pd.Series([1,2,3],index=[1,2,3],name='A')
s2 = pd.Series([10,20,30],index=[1,2,3],name='B')
s3 = pd.Series([100,200,300],index=[1,2,3],name='C')

#以键值对键入到Datarame,则series当作列加入
print('============以行的形式加入==========')
df_as_row=pd.DataFrame({s1.name:s1,s2.name:s2,s3.name:s3})
print(df_as_row)

#以数组形式添加到DataFrame，则Series当作行加入
print('========以行的形式加入========')
df_as_col = pd.DataFrame([s1,s2,s3])
print(df_as_col)

print('========索引不完全相同的情况========')
s1 = pd.Series([1,2,3],index=[1,2,3],name='A')
s2 = pd.Series([10,20,30],index=[1,2,3],name='B')
s3 = pd.Series([100,200,300],index=[2,3,4],name='C')

#以键值对键入到Datarame,则series当作列加入
print('============以行的形式加入==========')
df_as_row=pd.DataFrame({s1.name:s1,s2.name:s2,s3.name:s3})
print(df_as_row)

#以数组形式添加到DataFrame，则Series当作行加入
print('========以行的形式加入========')
df_as_col = pd.DataFrame([s1,s2,s3])
print(df_as_col)