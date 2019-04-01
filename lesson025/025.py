# E:\04ML\06SourceCode\awesome-pandas-practice\lesson025
import pandas as pd
import  matplotlib.pyplot as plt
def low_score_red(s):
    color = 'red' if s<60 else 'green'
    return f'color:{color}'

def highest_score_green2(col):
    return ['background-color:lime' if v==col.max() else 'background-color:red' for v in col]

students = pd.read_excel('E:/04ML/06SourceCode/awesome-pandas-practice/lesson025/Students.xlsx')
print(students.head(3))

students.style.applymap(low_score_red, subset=['Test_1', 'Test_2', 'Test_3'])#无差别施加到每个单元格

students.style.apply(highest_score_green2, subset=['Test_1', 'Test_2', 'Test_3'])#按照行和列的原则进行施加，默认为列


