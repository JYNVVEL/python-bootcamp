color_input = input('Please enter a color: ').lower()

match color_input:
    case 'green':
        print('Go')
    case 'yellow':
        print('Wait...')
    case 'red':
        print('Stop')
    case _:
        print('Malfunction')

