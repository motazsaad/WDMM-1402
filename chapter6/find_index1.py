'''
find the index of an char
'''

word = 'sound'
key = input('enter letter: ')
for i in range(len(word)):
    if word[i] == key:
        print(i)
