import pandas as pd
import  matplotlib.pyplot as plt

students = pd.read_excel('Students_Duplicates.xlsx',index_col='ID')
print(students)

#定位重复数据的位置
dupe = students.duplicated(subset='Name')
print(dupe[dupe==True].index)#dupe[dupe]
# print(students.iloc[24])#at 用于定位单元格
print(students.iloc[dupe[dupe].index-1])#参数代表位置，从0开始，注意和index的对应关系
print(students.loc[dupe[dupe].index])#参数代表某行的index标签


print(students.drop_duplicates(subset='Name',inplace=True,keep='first'))

print(students)

