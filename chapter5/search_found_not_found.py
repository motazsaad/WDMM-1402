L1 = [9, 41, 12, 3, 74, 15, 20, 21, 7]
number = int(input('search for: '))
found = False
for i in L1:
    if i == number:
        found = True
        break
    print('i=', i, 'found', found)
    print('---------------------')
if found:
    print('found')
else:
    print('not found')
