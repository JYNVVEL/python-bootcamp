correct_password = 'pass'

password = None
incorrect = password != correct_password

while incorrect:
    password = input('Enter password: ')
