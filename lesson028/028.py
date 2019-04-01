import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

page_001 = pd.read_excel('Students.xlsx',sheet_name='Page_001')
page_002 = pd.read_excel('Students.xlsx',sheet_name='Page_002')

students = pd.concat([page_001,page_002]).reset_index(drop=True)

# print(students)
#增加一列，数据赋值用np.arange
students['Age'] = np.arange(0,len(students))

#删除列
students.drop(columns=['Age','Score'],inplace=True)

#插入列
students.insert(1,column='Foo',value=np.repeat('foo',len(students)))

#对列进行改名
students.rename(columns={'Name':'NAME','Foo':'FOO'})

print()





