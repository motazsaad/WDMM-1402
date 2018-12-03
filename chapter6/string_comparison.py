# string comparison (alphabetic order)

word1 = 'banana'
word2 = input('enter a word: ')
if word2 > word1:
    print(word2, 'is after', word1)
elif word2 < word1:
    print(word2, 'is before', word1)
else:
    print(word2, 'is the same', word1)
