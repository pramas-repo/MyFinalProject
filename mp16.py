# format() function with specific data type {:d} {:f} {:s}
rno = 500
name = 'amol deshmukh'
per = 67.23

print("Rno = {:d}\nName = {:s}\nPercentage = {:.2f}".format(rno,name,per))
# padding of data
print("Rno = {:20d}\nName = {:20s}\nPercentage = {:20.2f}".format(rno,name,per))
# padding of data and left or right / center
print("Rno = {:<20d}\nName = {:<20s}\nPercentage = {:<20.2f}".format(rno,name,per))
# padding of data and left or right / center and replace blank spaces
print("Rno = {:*<20d}\nName = {:*<20s}\nPercentage = {:*<20.2f}".format(rno,name,per))