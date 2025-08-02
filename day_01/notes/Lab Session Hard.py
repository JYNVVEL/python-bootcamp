def get_number():
    valid = False
    number = 0
    while not valid:
        user_input = input('Enter a number: ')
        try:
            number = int(user_input)
            if number < 0:
                raise ValueError()
            valid = True

        except ValueError:
            print('Enter a valid number!')

    return number

valid_number = get_number()