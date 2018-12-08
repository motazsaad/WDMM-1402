'''
اكتب برنامج لـطباعة التالي من نص
- عدد الكلمة I
- عدد الكلمات بالاحرف الكبيرة
- عدد الكلمات بالاحرف الصغيرة
- عدد الاحرف الخاصة special chars
'''
text = ''' Hi , my name is Ahmed , and 
I like banana , Orange , 
and apple fruits - but I do not like 
APPLE COMPANY !!!
I love Python , and python is cool ! :)
I AM A PYTHON PROGRAMMER ! OK 
please share , comment #python ;)   
'''
words = text.split()
print('word count', len(words))
i_count = 0
upper_count = 0
lower_count = 0
special_count = 0
for word in words:
    if word is 'I':
        i_count = i_count + 1
    if word.isupper():
        upper_count = upper_count + 1
    if word.islower():
        lower_count = lower_count + 1
    if not word.isalnum():
        special_count = special_count + 1
print('I count:', i_count)
print('lower count', lower_count)
print('upper count', upper_count)
print('special count', special_count)
