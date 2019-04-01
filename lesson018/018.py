import pandas as pd
import matplotlib.pyplot as plt

employees = pd.read_excel('Employees.xlsx')
print(employees.head(3))


df = employees['Full Name'].str.split(n=0,expand=True)#分割成几列,n为切出后保留的列数,为0或-1表示全部保留
print(df)

employees['Fist Name'] = df[0]#列名，dataframe中括号索引中必须是列名
employees['Last Name'] = df[1].str.upper()

print(employees)
