'''
اكتب برنامج لعد الكلمات في نص بحيث تبدأ بحرف m وتنتهي بحرف متحرك (a e i o u ) سواء كان الحرف كبير ام صغير
'''

text = ''' Hi , my name is Ahmed , and 
I like banana , Orange , 
and apple fruits - but I do not like 
APPLE COMPANY !!!
I love Python , and python is cool ! :)
I AM A PYTHON PROGRAMMER ! OK 
please share , comment #python ;)   
'''
count = 0
vowels = 'aeiou'
for word in text.split():
    small_word = word.lower()
    if small_word.startswith('a') and small_word[-1] in vowels:
        count += 1
print(count)
