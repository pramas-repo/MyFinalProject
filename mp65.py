# 3. dict in python - data enclosed in {} and dict mutable
# 1. Accessing elements in dict
student = {'rno':200, 'name':'Yogesh','age':20,'marks':450.30} # dict with key-value pair
# A. Access complete dict
print(student)  
# B. Accessing elements using key index - dict does not support index, 
print(student['name'])  # Yogesh
print(student['age'])   # 20
# C. Slicing of dict - dict does not support slicing because it does not support index