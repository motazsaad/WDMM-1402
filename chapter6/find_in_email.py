'''
write a program to extract the following information:
- domain
- username
- year
'''

emails = ['From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008',
          'From msaad@iugaza.edu.ps Sat Jan  5 09:14:12 2017',
          'From motaz@google.com Sat Dec  11 09:14:11 2018']
for email in emails:
    at_pos = email.find('@')
    sp_pos = email.find(' ', at_pos)
    domain = email[at_pos + 1:sp_pos]
    print('domain:', domain)
    ################
    sp_pos = email.find(' ')
    user = email[sp_pos + 1:at_pos]
    print('user:', user)
    year = email[-4:]
    print('year:', year)
