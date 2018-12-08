'''
اكتب برنامج لطباعة
- عدد المسافات
- عدد الاحرف الكبيرة
- عدد الاحرف الصغيرة
في نص

'''
text = ''' Hi , my name is Ahmed , and 
I like banana , Orange , 
and apple fruits - but I do not like 
APPLE COMPANY !!!
I love Python , and python is cool ! :)
I AM A PYTHON PROGRAMMER ! OK 
please share , comment #python ;)   
'''
space_count = 0
upper_count = 0
lower_count = 0
for char in text:
    if char.isspace():
        space_count += 1
    if char.islower():
        lower_count += 1
    if char.isupper():
        upper_count += 1
print('space count', space_count)
print('upper count', upper_count)
print('lower count', lower_count)
