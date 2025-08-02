role = input('Enter role: ').lower()

if role == 'admin' or role == 'editor':
    print('Edit access enabled')
else:
    print('Edit not allowed')

