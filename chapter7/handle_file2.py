'''

اكتب برنامج لقراءة ملف واستخراج الـ domain  من الأسطر التي تبدأ بكلمة From . ملاحظة: يجب كتابة كود استخراج الـ domain  في دالة واستدعائها في البرنامج

'''


def get_domain(text):
    at_pos = text.find('@')
    sp_pos = text.find(' ', at_pos)
    domain = text[at_pos + 1:sp_pos]
    return domain


#################################


mail_file = open('mbox.txt', 'r')
# read file line by line
for line in mail_file:
    if line.startswith('From:'):
        print(get_domain(line))
