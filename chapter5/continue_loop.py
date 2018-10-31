while True:
    line = input('> ')
    if line[0] == '#':  # line[0] is the 1st letter
        continue  # go to line 1
    if line == 'done':
        break  # go to line 8
    print(line)
print('Done!')
print('done again! ')
