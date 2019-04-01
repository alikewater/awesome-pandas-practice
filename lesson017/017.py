import pandas as pd
import matplotlib.pyplot as plt

def score_validation(row):
    try:
        assert 0<=row.Score<=100
    except:
        print('#',(row.ID),'\t student ',(row.Name),' has invalidate score ',(row.Score),'.')

def score_validation01(row):
    if not 0<=row.Score<=100:
        print('#', (row.ID), ' student ', (row.Name), ' has invalidate score ', (row.Score), '.')


students = pd.read_excel('Students.xlsx')
print(students.head(3))

students.apply(score_validation,axis=1)#轴的意思，0从上倒下，1从左到右

