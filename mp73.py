# Methods in Dictionary
# copy() = Returns a shallow copy of the dictionary
employee = {'eno':10, 'name':'Rajesh Rathi','age':27,'salary':25000}
employee1 = employee.copy()
print(employee)
print(employee1)
# get() = Returns the value of the specified key
print(employee.get('name'))
print(employee['name'])
# items() = Returns a list containing a tuple for each key value pair
print(employee.items()) #  used in for loop to access key and value
# keys() = Returns a list containing the dictionary's keys
print(employee.keys())
# values() = Returns a list of all the values in the dictionary
print(employee.values())