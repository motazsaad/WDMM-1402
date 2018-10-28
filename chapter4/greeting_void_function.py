'''
write a program that greet people in their languages.
Arabic, English, Turkish, Spanish, French, portuguese
'''


def greeting(name, lang):
    if lang == 'ar':  # Arabic
        print('مرحباً', name)
    elif lang == 'en':  # English
        print('hello', name)
    elif lang == 'es':  # Español
        print('hola', name)
    elif lang == 'tr':  # Turkish
        print('merheba', name)
    elif lang == 'fr':  # French
        print('bonjour', name)
    elif lang == 'pt':  # Portuguese
        print('Olá', name)
    else:  # English
        print('hello', name)


greeting('David', 'en')
greeting('Denis', 'fr')
greeting('أحمد', 'ar')
greeting('Cristiano', 'es')
greeting('Mohmet', 'tr')
greeting('Alberto', 'it')
