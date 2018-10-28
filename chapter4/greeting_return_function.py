'''
write a program that greet people in their languages.
Arabic, English, Turkish, Spanish, French, portuguese.
Note: use return function
'''


def greeting(lang):
    if lang == 'ar':  # Arabic
        return 'مرحبا'
    elif lang == 'en':  # English
        return 'hello'
    elif lang == 'es':  # Español
        return 'hola'
    elif lang == 'tr':  # Turkish
        return 'merheba'
    elif lang == 'fr':  # French
        return 'bonjour'
    elif lang == 'pt':  # Portuguese
        return 'Olá'
    else:  # English
        return 'hello'


print(greeting('ar'))
print(greeting('ar'), 'أحمد')
print(greeting('es'))
print(greeting('es') + ' Alberto')
name = input('enter your name: ')
print(greeting('tr'), name)

greeting_tr = greeting('tr')
print('greeting in turkish', greeting_tr)
