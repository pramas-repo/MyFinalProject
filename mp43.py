# iterator with for loop
# iterators in python
names = ['ajay','sunil','pooja','yogesh','aarti','rajesh'] # list
it = iter(names)

# normal for loop as collection loop without iterator
for i in names:
    print(i,end=' ')
print()
# for loop with an iterator - the for loop does not require next()   
for i in it:
    print(i,end=' ')