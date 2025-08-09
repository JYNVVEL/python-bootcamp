class NotANumberError(ValueError):
    def __init__(self):
        super().__init__("Please enter a valid number")

class NotPositiveNumberError(ValueError):
    def __init__(self):
        super().__init__("Please enter a positive number")

class NotWithinRangeError(ValueError):
    def __init__(self):
        super().__init__("Please enter a number from 1 to 100")

user_input = input("Enter a number from [1, 100]: ")

is_numeric = user_input.replace(".","").isnumeric()
is_numeric_sign = user_input[1:].replace(".","").isnumeric()

if not is_numeric and not is_numeric_sign:
    raise NotANumberError()

if "." in user_input:
    number = float(user_input)
else:
    number = int(user_input)

if number < 0:
    raise NotPositiveNumberError()

if not (0 <= number <= 100):
    raise NotWithinRangeError()
