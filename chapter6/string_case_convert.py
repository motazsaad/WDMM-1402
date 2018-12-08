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
print('text:', text)
for word in text.split():
    if word.islower():
        print(word.upper())
    elif word.isupper():
        print(word.lower())
    else:
        print(word)
