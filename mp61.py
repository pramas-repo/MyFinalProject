# 2. Tuples in Python - data eclosed in () and tuple immutable
colors = ('red','yellow','green','blue','pink')
prices = (200.45, 450.30, 10000.90, 500.00, 100.00)
# 1. Accessing elements in tuple
# A. Access complete
print(colors)
print(prices)
# B. Accessing elements using index
print(colors[3]) # blue
print(prices[1]) # 450.30
# C. Slicing of tuple
print(colors[1:4]) # ('yellow', 'green', 'blue')
print(prices[2:4]) # (10000.90, 500.00)
# D. Accessing elements using negative index
print(colors[-1]) # pink
print(prices[-2]) # 500.00
print(colors[-3:-1]) # ('green', 'blue')