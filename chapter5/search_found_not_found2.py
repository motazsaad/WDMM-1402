L1 = [9, 41, 12, 3, 74, 15, 20, 21, 7]
number = int(input('search for: '))
result = 'not found'
for i in L1:
    if i == number:
        result = 'found'
        break
    print(i, result)
print(result)
