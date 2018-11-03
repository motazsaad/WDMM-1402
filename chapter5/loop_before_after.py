count = 0
total = 0
print('count (before):', count)
print('total (before):', total)
for element in [9, 41, 12, 3, 74, 15]:
    count = count + 1
    total = total + element
    print(count, element)
print('count (after):', count)
print('total (after):', total)
print('average:', total / count)
