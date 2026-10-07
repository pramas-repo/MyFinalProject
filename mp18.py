# input() function to input data from keyword
# input() function enters any data as a string
name = input('Enter Your Name : ')
rno = int(input('Enter Your Rno : '))
per = float(input('Enter Your Percentage : '))

print('Rno = {} Name = {} Per = {}'.format(rno,name,per))
print(type(name))
print(type(rno))
print(type(per))