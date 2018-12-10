text = ''' Hi , my name is Ahmed , and 
I like banana , Orange , 
and apple fruits - but I do not like 
APPLE COMPANY !!!
I love Python , and python is cool ! :)
I AM A PYTHON PROGRAMMER ! OK 
please share , comment #python ;)   
'''
count = 0
vowels = 'aeiouAEIOU'
letter = 'aA'
for word in text.split():
    if word[0] in letter and word[-1] in vowels:
        count += 1
print(count)
