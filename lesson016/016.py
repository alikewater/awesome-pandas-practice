import pandas as pd
import matplotlib.pyplot as plt

students = pd.read_excel('Student_Score.xlsx',sheet_name='Students',index_col='ID')
scores = pd.read_excel('Student_Score.xlsx',sheet_name='Scores',index_col='ID')
print(students.head(3))
print(scores.head(3))


#使用merge进行数据联合
# table = students.merge(scores,on='ID')#默认模式为innerjoin
# print(table)

#left outer Join
table = students.merge(scores,left_on='ID',right_on='ID',how='left').fillna(0)#列名不同可以使用lefton，righton
table = students.merge(scores,left_on= students.index,right_on=scores.index,how='left').fillna(0)#制定索引列进行联立

# table = students.merge(scores,on='ID',how='left').fillna(0)#列名相同时
# table = students.merge(scores,how='left').fillna(0)#默认不指定，自动寻找相同列名（普通列中寻找，不能自动寻找索引列）

#列名不同可以使用lefton，righton，当on参数不指定时，列名不能是索引列
table.Score.astype(int)
print(table)


#join默认采用index列进行联立,没有left_on和right_on参数
table = students.join(scores,on='ID',how='left').fillna(0)#
table = students.join(scores,how='left').fillna(0)#可以不指定join列，默认采用索引列

print(table)




