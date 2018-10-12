x = 5  # main flow
if x > 2:
    print('Bigger than 2')  # block 1
    print('Still bigger')  # block 1
print('Done with 2')

for i in range(5):
    print(i)  # # block 2
    if i > 2:  # block 2
        print('Bigger than 2')  # block 3 (inside block 2)
    print('Done with i', i)  # block 2
print('All Done')  # main flow
