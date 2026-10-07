# find largest in 3 numbers
a, b, c = map(int,input('Enter 3 numbers : ').split()) 

if a > b and a > c:
    print('Large number is {}'.format(a))
elif b > c:
    print('Large number is {}'.format(b))
else:
    print('Large number is {}'.format(c))        