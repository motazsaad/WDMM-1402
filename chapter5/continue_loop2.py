ans = 'yes'
while ans == 'yes':
    line = input('> ')
    if line[0] == '$':
        continue  # go to line 1
    print(line)
    ans = input('again yes/no?: ')
