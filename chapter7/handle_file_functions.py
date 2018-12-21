'''
اكتب برنامج لقراءة ملف واستخراج الـ domain واسم المستخدم والسنة من الأسطر التي تبدأ بكلمة From . ملاحظة: يجب كتابة كود استخراج الـ domain  واسم المستخدم والسنة في دوال واستدعائها في البرنامج

'''


def get_domain(text):
    at_pos = text.find('@')
    sp_pos = text.find(' ', at_pos)
    return text[at_pos + 1:sp_pos]


def get_user(text):
    sp_pos = text.find(' ')
    at_pos = text.find('@')
    return text[sp_pos + 1:at_pos]


def get_year(text):
    text = text.strip()
    return text[-4:]
#################################


mail_file = open('mbox.txt', 'r')
# read file line by line
for line in mail_file:
    if line.strip().startswith('From '):
        print('domain:', get_domain(line))
        print('user:', get_user(line))
        print('year:', get_year(line))
        print('-----------------------')
