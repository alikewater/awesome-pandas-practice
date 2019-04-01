import pandas as pd


def age_18_to_35(a):
    return 18<=a<35;

def level_a(a):
    return 85<=a<=100


students = pd.read_excel('Students.xlsx',index_col='ID')
# # print(students)
#
#
# # print(students['Age'].apply(age_18_to_35))
#
# students = students.loc[students['Age'].apply(age_18_to_35)]
# print(students['Score'].apply(level_a))
# #
# # students = students.loc[students['Score'].apply(level_a)]
# students = students.loc[students['Score'].apply(level_a)]
# print(students)

students = students.loc[students['Age'].apply(lambda x:  18<=x<35)] \
    .loc[students['Score'].apply(lambda x:  85<=x<=100)]
#
print(students)
# print(students.Age.apply(lambda a: 18<=a<35))

