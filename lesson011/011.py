import  pandas as pd
import matplotlib.pyplot as plt

users = pd.read_excel('Users.xlsx',index_col='ID')
users['Total'] = users['Oct']+users['Nov']+users['Dec']
users.sort_values(by='Total',ascending=False,inplace=True)
print(users)

#垂直绘制
users.plot.bar(x='Name',y=['Oct','Nov','Dec'],stacked=True,title='User Behavior')
plt.xlabel('User No',fontweight='bold')
plt.ylabel('Number',fontweight='bold')

ax = plt.gca()
ax.set_xticklabels(users.Name,rotation='45',ha='right')
plt.tight_layout()

fig = plt.gcf()
fig.savefig('userbehevior_v.jpg')

#水平绘制
users.sort_values(by='Total',ascending=True,inplace=True)
users.plot.barh(x='Name',y=['Oct','Nov','Dec'],stacked=True,title='User Behavior')
plt.xlabel('User No',fontweight='bold')
plt.ylabel('Number',fontweight='bold')

ax = plt.gca()
ax.set_yticklabels(users.Name,rotation='45',va='top')
plt.tight_layout()

fig = plt.gcf()
fig.savefig('userbehevior_h.jpg')

plt.show()