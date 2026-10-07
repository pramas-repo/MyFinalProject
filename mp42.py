# iterators in python
#  it
names = ['ajay','sunil','pooja','yogesh','aarti'] # list
it = iter(names)

print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
it = iter(names)
print(next(it))