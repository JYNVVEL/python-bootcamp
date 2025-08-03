email_input = input("Enter your email address: ")
email_input = email_input.split()
email_input = " ".join(email_input)

if email_input.endswith("@gmail.com"):
    print("This is a valid gmail address")
else:
    print("This is NOR a valid gmail address")
