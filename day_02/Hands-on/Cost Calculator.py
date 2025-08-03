import json
def spend(expenses, cost):
    """Add a new cost in the list of expenses"""
    expenses.append(cost)

def refund(expenses):
    """Remove the last cost added (if any)"""
    expenses.pop(-1)

def show(expenses):
    """Print the list of expenses and the total cost"""
    print('=' * 100)
    for expense in expenses:
        print(expense)
    print(f"Total: {sum(expenses)}")

def save(expenses, filepath):
    with open(filepath, "w") as file:
        for expense in expenses:
            file.write(str(expense) + "\n")
        file.write("Total: " + str(sum(expenses)))






def main():
    current_expenses = []
    command = input("Command: ")

    while command:
        # Handle command here
        if command == 'spend':
            cost = int(input('Enter Cost:'))
            spend(current_expenses, cost)
        elif command == 'refund':
            refund(current_expenses)
        elif command == 'show':
            show(current_expenses)
        elif command == "save":
            filepath = input('Enter Filepath: ')
            save(current_expenses, filepath)
        # Ask for more
        command = input("Command: ")



main()