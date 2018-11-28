word = list('banana')
print('word before', word)
for i in range(len(word)):
    if word[i] == 'a':
        word[i] = 'b'
print('word after', word)
