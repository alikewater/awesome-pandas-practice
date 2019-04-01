import pandas as pd
import matplotlib.pyplot as plt

pd.options.display.max_columns = 777
students = pd.read_excel('Students.xlsx',index_col='ID')
print(students.head(3))

temp = students[['Test_1','Test_2','Test_3']]
row_sum = temp.sum(axis=1)
row_mean = temp.mean(axis =1)
# print(row_sum)
# print(row_mean)

students['Total'] = row_sum
students['Avg'] = row_mean
# students.append({'Avg':row_mean})


col_mean = students[['Test_1','Test_2','Test_3','Total','Avg']].mean()
col_mean['Name'] = 'Summary'
students = students.append(col_mean,ignore_index=True)

print(students)


