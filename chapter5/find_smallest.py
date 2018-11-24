l1 = [9, 41, 12, 3, 74, 15]
smallest = None
print('Before')
for value in l1:
    if smallest is None:
        smallest = value
    elif value < smallest:
        smallest = value
    print(smallest, value)
print('After', smallest)
