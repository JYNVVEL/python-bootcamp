count = 0
running = True

while running:
    choice = input('Provide command: ')
    match choice:
        case 'add':
            print(choice)
            count+=1
            print(count)
        case 'sub':
            print(choice)
            count-=1
            print(count)
        case 'double':
            print(choice)
            count*=2
            print(count)
        case 'exit':
            print('exit ')

