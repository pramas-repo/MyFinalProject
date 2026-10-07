# enter marks ph, ch, ma
ph, ch, ma = map(int,input('Enter Phy, Che, Maths : ').split())

gt = ph + ch + ma
per = gt / 3.0
print(f'Total = {gt} Per = {per}')