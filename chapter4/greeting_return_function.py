'''
write a program that greet people in their languages.
Arabic, English, Turkish, Spanish, French, portuguese.
Note: use return function
'''


def greeting(lang):
    if lang == 'ar':
        return 'مرحبا'
    elif lang == 'en':
        return 'hello'
    elif lang == 'es':
        return 'hola'
    elif lang == 'tr':
        return 'merheba'
    elif lang == 'fr':
        return 'bonjour'
    elif lang == 'pt':
        return 'Olá'
    else:
        return 'hello'


print(greeting('ar'))
print(greeting('ar'), 'أحمد')
print(greeting('es'))
print(greeting('es') + ' Alberto')
name = input('enter your name: ')
print(greeting('tr'), name)

greeting_tr = greeting('tr')
print('greeting in turkish', greeting_tr)
