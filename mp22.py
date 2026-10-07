# simple interest calculation using input() function
amt, years, rate = map(float, input('Enter Amount, years and rate : ').split())

simp = (amt * years * rate) / 100
print("Amount = {} Years = {} Rate of Interest = {} Interest = {}".format(amt,years,rate,simp))
