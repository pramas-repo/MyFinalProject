# 1. Lists in Python
# Create a list
subs = ['physics','chemistry','maths','biology']

# Accessing list using for loop without iterator
for s in subs:
    print(s,end=' ')
print()
# Accessing list using for loop with iterator
it = iter(subs)
for s in it:
    print(s,end=' ')
