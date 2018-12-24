'''
اكتب برنامج لقراءة ملف وطباعة الاسطر التي تحتوي على هذا ال domain
'''

domain = '@uct.ac.za'
# solution 1 (continue)
fhand = open('mbox-short.txt', 'r')
for line in fhand:
    line = line.strip()
    if domain not in line:
        continue
    print(line)
print('-----------------------------')
# solution 2 (without continue)
fhand = open('mbox-short.txt', 'r')
for line in fhand:
    line = line.strip()
    if domain in line:
        print(line)
