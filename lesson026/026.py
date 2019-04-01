# E:\04ML\06SourceCode\awesome-pandas-practice\lesson025
import pandas as pd
import  matplotlib.pyplot as plt
import seaborn as sns

students = pd.read_excel('E:/04ML/06SourceCode/awesome-pandas-practice/lesson025/Students.xlsx')
print(students.head(3))

color_map = sns.light_palette('green', as_cmap=True)
students.style.background_gradient(cmap=color_map, subset=['Test_1','Test_2','Test_3'])




