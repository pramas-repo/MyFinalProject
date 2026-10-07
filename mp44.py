# iterator with while loop
# iterators in python
names = ['ajay','sunil','pooja','yogesh','aarti','rajesh'] # list
it = iter(names)

while True: # continuos loop
    try:
        print(next(it))
    except:
        break    
