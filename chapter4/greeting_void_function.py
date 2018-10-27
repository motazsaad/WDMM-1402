'''
write a program that greet people in their languages.
Arabic, English, Turkish, Spanish, French, portuguese
'''


def greeting(name, lang):
    if lang == 'ar':
        print('مرحباً', name)
    elif lang == 'en':
        print('hello', name)
    elif lang == 'es':
        print('hola', name)
    elif lang == 'tr':
        print('merheba', name)
    elif lang == 'fr':
        print('bonjour', name)
    elif lang == 'pt':
        print('Olá', name)
    else:
        print('hello', name)


greeting('David', 'en')
greeting('Denis', 'fr')
greeting('أحمد', 'ar')
greeting('Cristiano', 'es')
greeting('Mohmet', 'tr')
greeting('Alberto', 'it')
