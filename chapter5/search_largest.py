L1 = [9, 41, 12, 3, 74, 15]
largest_so_far = -1
for i in L1:
    if i > largest_so_far:
        largest_so_far = i
    print('i=', i, 'largest:', largest_so_far)

print('largest so far:', largest_so_far)
