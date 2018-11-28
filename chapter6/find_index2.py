'''
find the index of an char, and indicate if it is not found
'''
word = 'sound'
key = input('enter letter: ')
# 1. define var
position = -1
# 2. loop
for i in range(len(word)):
    if word[i] == key:
        position = i
# 3. print result
if position is -1:
    print('not found')
else:
    print(position)
