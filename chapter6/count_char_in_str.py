word = 'banana'
char = input('enter a char: ')
count = 0
for i in range(len(word)):
    if word[i] is char:
        count = count + 1
print(count)
