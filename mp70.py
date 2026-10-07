# Dict in python
employee = {'eno':10, 'name':'Rajesh Rathi','age':27,'salary':25000}
# 1. Access a dict
# a. Acess complete dict
print(employee) 
# delete all data from dict and make it empty
employee.clear()
print(employee)
# delete dict completely
del employee
print(employee)  # This will raise an error since employee dict is deleted