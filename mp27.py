# calculator program
a, b = map(int,input('Enter any two numbers : ').split())
op = input('Enter Operator (+, - * /) : ')

if op == '+':
    res = a + b
    print('Result = {}'.format(res))
elif op == '-':    
    res = a - b
    print('Result = {}'.format(res))
elif op == '*':    
    res = a * b
    print('Result = {}'.format(res))
elif op == '/':    
    res = a / b
    print('Result = {}'.format(res))   
else:
    print('Wrong operator entered')         