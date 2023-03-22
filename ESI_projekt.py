import pandas as pd
from math import log2 
from projektBFG import build_tree

names = ['StudentStatus', 'NoStudentStatus', 'NoEducation', 'Bachelor', 'Master', 'AcademicExperience', 'NoExperience', 'ComercialExperience', 'BasicEnglish', 'AdvancedEnglish', 'FluentEnglish',  'Python', 'R', 'Java', 'HTML', 'Decision']
# data = pd.read_csv('dane.csv', delimiter=';', index_col=False)
test = pd.read_csv('test.csv', delimiter=';', index_col=False)

# No position - No (0)
# Data Analyst - Da (1)
# UX/UI designer - Ux (2)
# Software developer - Sd (3)

decisions = ['No position', 'Data Analyst', 'UX/UI designer', 'Software developer']

tree = build_tree(test)
print(tree)