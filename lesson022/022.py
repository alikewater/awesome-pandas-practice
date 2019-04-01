import pandas as pd
import  matplotlib.pyplot as plt

# students_excel = pd.read_excel('Students.xlsx',index_col='ID');
students_csv = pd.read_csv('Students.csv',index_col='ID')
students_tsv = pd.read_csv('Students.tsv',sep='\t',index_col='ID')
students_txt = pd.read_csv('Students.txt',sep='|',index_col='ID')

print(students_csv.head(3))
print(students_tsv.head(3))
print(students_txt.head(3))



