import pandas as pd

page_001 = pd.read_excel('Students.xlsx',sheet_name='Page_001')
page_002 = pd.read_excel('Students.xlsx',sheet_name='Page_002')

print(page_001.head(3))
print(page_002.head(3))

students = page_001.append(page_002).reset_index(drop=True)
# print(students)

# stu = pd.Series({'ID':41,'Name':'Abel','Score':80})
# students = students.append(stu,ignore_index=True)
# print(students.tail(1))
#
# #通过at和iloc定位出来的记录是可以写入的
# #通过单元格进行修改
# students.at[39,'Name'] = 'Balley'
# students.at[39,'Score'] = 120
#
# #整行替换
# stu = pd.Series({'ID':40,'Name':'Balley','Score':120})
# students.iloc[39] = stu
#
# #在中间插入一条记录
# stu = pd.Series({'ID':101,'Name':'Danie','Score':101})
#
# part1 = students[:20]
# part2 = students[20:]
# students = part1.append(stu,ignore_index=True).append(part2).reset_index(drop=True)
#
#
# #删除行
# # students.drop(index=range(0,10),inplace=True)
# students.drop(index=students[0:10].index,inplace=True)
#
#条件删除
for i in range(5,15):
    students.at[i,'Name'] = ''
# print(students)
#
# #方式1,通过获取索引，并使用drop去掉相应索引的部分
# missing = students.loc[students['Name']=='']
# students.drop(missing.index,inplace=True)
# students = students.reset_index(drop=True)

#方式2，通过获取需要切片的条件(索引数组或者bool数组)，通过切片的方式实现
print(students['Name']=='')
students = students[students['Name']!='']
print(students)


