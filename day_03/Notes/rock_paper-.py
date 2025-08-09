class InvalidChoiceError(ValueError):
    def __init__(self, choice):
        super().__init__(f"You chose {choice}. Please pick a valid choice.")

choices = ("rock", "paper", "scissors")
user_input = input("Enter your choice: ")

if user_input not in choices:
    raise InvalidChoiceError(user_input)