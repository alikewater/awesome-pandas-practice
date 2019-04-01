import pandas as pd
import matplotlib.pyplot as plt


students = pd.read_excel('Students.xlsx')

students.sort_values(by='Number',ascending=False,inplace=True)
print(students)

# #采用datarame的绘图
# students.plot(kind='bar',x='Field',y='Number',color='orange',title='International Field by Number')
# students.plot.bar(x='Field',y='Number',color='orange',title='International Field By Number')
# plt.tight_layout()#紧凑格式，名称可以显示全
# plt.show()

#采用原生plt绘图
plt.bar(students.Field,students.Number,color='orange')
plt.xticks(students.Field,rotation='90')
plt.xlabel('Field')
plt.ylabel('Number')
plt.title('International Field by Number')
plt.tight_layout()#紧凑格式，名称可以显示全
plt.show()

