word = list('banana')  # ['b', 'a', 'n', 'a', 'n', 'a']
print('word before', word)
for i in range(len(word)):
    if word[i] == 'a':
        word[i] = 'b'
print('word after', word)
