# 3. dict in python - data enclosed in {} and dict mutable
# 1. Accessing elements in dict
student = {'rno':200, 'name':'Yogesh','age':20,'marks':450.30} # dict with key-value pair
# 4. Access dict using for loop
for key in student:
    print(key,end=' ')
print()
for value in student.values(): # dict.values() returns all values in dict
    print(value,end=' ')    
print()
for key, value in student.items(): # dict.items() returns all key-value pair in dict
    print(key,'=',value,end=' ')