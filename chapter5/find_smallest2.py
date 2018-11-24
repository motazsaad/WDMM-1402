l1 = [9, 41, 12, 3, 74, 15]
smallest = l1[0]
print('Before')
for value in l1:
    if value < smallest:
        smallest = value
    print(smallest, value)
print('After', smallest)
