# Padding of data and align left right or center using format() function
name = 'sameer'
rno = 100
per = 78.12
# < make data left aligned, > makes right aligned and ^ make it center align
print("Rno = {:<20}\nName = {:<20}\nPer = {:<20}".format(rno,name,per))
print("Rno = {:>20}\nName = {:>20}\nPer = {:>20}".format(rno,name,per))
print("Rno = {:^20}\nName = {:^20}\nPer = {:^20}".format(rno,name,per))