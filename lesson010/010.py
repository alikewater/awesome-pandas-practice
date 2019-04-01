import pandas as pd
import matplotlib.pyplot as plt

students = pd.read_excel('Students.xlsx')
print(students)
# students.drop(columns='2016')

students.sort_values(by='2017',inplace=True,ascending=True)
students.plot.bar(x ='Field',y=['2016','2017'],color=['orange','red'])
# students.plot.bar(x ='Field',y='2017',color='orange')

# plt.xticks(students.Field)
plt.title('International Students By Field',fontsize=18,fontweight='bold')
plt.xlabel('Field',fontsize=10,fontweight='bold')
plt.ylabel('Number',fontsize=10,fontweight='bold')
# plt.tight_layout()

#获取绘图的轴
ax = plt.gca()
ax.set_xticklabels(students.Field,rotation='45',ha='right')

#获取绘图的子图
fig = plt.gcf()
fig.subplots_adjust(left=0.2,bottom=0.42)

fig.savefig('groupbar.jpg')

plt.show()


