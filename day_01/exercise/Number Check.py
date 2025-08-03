user_input = input("Enter Number: ").strip()
user_input = user_input.replace(",","")
user_input = user_input.split()
user_input = " ".join(user_input)

if user_input.isnumeric():
    user_input = int(user_input)
    print(user_input + 1)
else:
    print("Please enter a valid number")