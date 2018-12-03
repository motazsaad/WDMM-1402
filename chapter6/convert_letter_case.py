words = ['apple', 'Orange', 'TOMATO', 'mango']
for word in words:
    if word.isupper():
        print(word.lower())
    elif word.islower():
        print(word.upper())
    else:
        print(word)
