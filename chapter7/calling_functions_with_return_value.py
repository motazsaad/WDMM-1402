def is_vowel(word):
    vowels = 'aeiouAEIOU'
    return word[0] in vowels


# call a function with return value
# method 1: assign to a variable
result = is_vowel('apple')
# method 2: print
print(is_vowel('apple'))
print(is_vowel('banana'))
# method 3: wrong method
is_vowel('apple')

# it is like, save the cleaned text
text = ' hello '
text = text.strip()
