# Access data in tuple using for loop
colors = ('red','yellow','green','blue','pink')
prices = (200.45, 450.30, 10000.90, 500.00, 100.00)
# without iterator for loop
for c in colors:
    print(c,end=' ')
print()
# with iterator for loop
it = iter(prices)
for p in it:
    print(p,end=' ')        
print()