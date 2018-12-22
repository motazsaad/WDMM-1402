def is_vowel(my_word):
    vowels = 'aeiouAEIOU'
    return my_word[0] in vowels


#####################################


my_file = open('file_example.txt', 'r')
text = my_file.read()
vowel_count = 0
for word in text.split():
    if is_vowel(word):
        vowel_count += 1
print('vowel count:', vowel_count)
