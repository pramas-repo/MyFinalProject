# Fibonacci Number series - 0 1 1 2 3 5 8 13 21 .....
a = 0
b = 1
n = int(input('Enter a number : ')) # 5

print(f'{a} {b}',end=' ') # 0 1 
i = 1
while i <=n-2: # 3
    c = a + b # 1 2 3
    print(f'{c}', end=' ') # 1 2 3 5
    a = b # 1 2
    b = c # 2 3
    i+=1