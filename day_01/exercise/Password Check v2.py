correct_password = 'pass'

password_input = input('Please provide password: ')
correct_password_given = password_input == correct_password

if correct_password_given:
    print('Access Granted')
else:
    print('Access Denied')