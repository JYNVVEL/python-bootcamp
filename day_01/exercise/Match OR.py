color = input('Enter a color: ')

match color:
    case 'green' | 'GREEN':
        print('Go')
    case 'yellow' | 'YELLOW':
        print('Wait...')
    case 'red' | 'RED':
        print('Stop')
