# another example of continue statement
text = "I live in amravati city in maharashtra"
for i in text:
    if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
        continue
    print(i,end=' ')
