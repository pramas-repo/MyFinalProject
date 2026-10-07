# Dict in python
employee = {'eno':10, 'name':'Rajesh Rathi','age':27,'salary':25000}
# 1. Access a dict
# a. Acess complete dict
print(employee)
# b. Access a value using key
print(employee['name'])
print(employee['age'])
print(employee['salary'])
# c. Slicing of dict is not possible since it does not numeric index
# d. for loop to access dict
for key in employee:
    print(key)
print()
for value in employee.values():
    print(value)    
print()
for key, value in employee.items():
    print(key, value)    
