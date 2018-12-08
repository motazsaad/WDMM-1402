'''
اكتب برنامج لتحويل الكلمات بالاحرف الكبيرة الى احرف صغيرة والعكس
الكلمات التي لا تحقق الشرط تبقى كما هي

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
print(words)
for i in range(len(words)):
    if words[i].islower():
        words[i] = words[i].upper()
    elif words[i].isupper():
        words[i] = words[i].lower()
print(words)
