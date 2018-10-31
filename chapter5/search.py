l = [1, 3, 5, 6, 7, 99, 103]
print('list: ', l)
print('size: ', len(l))

key = int(input('please the number your search: '))
for number in l:
    if number == key:
        print(key, 'found')
        break
