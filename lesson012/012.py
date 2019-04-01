import pandas as pd
import matplotlib.pyplot as plt

students= pd.read_excel('Students.xlsx',index_col='From')#指定索引列
print(students)

#饼图绘制只需要一列数据，即一个Series,或Datarame的一列

#这里不能用点，因为2017不能作为变量名称，默认饼图的标识采用索引列，
# 因此需要在读取时将要显示的表示设置为索引列
# students.plot.pie('2017')
# students['2017'].sort_values(ascending=True).plot.pie(fontsize=8,startangle=-270)#设置气势角度调整顺时针旋转
students['2017'].sort_values(ascending=True).plot.pie(fontsize=3,startangle=-270)#设置气势角度调整顺时针旋转

plt.title('Students From Field',fontsize=18,fontweight='bold')
plt.ylabel('2017',fontsize=12,fontweight='bold')
# plt.tight_layout()
plt.show()