try:
    divider = int(input('Number: '))
    budget = 1000
    print(budget / divider)
except ValueError:
    print('Enter a valid number!')
except ZeroDivisionError:
    print("You can't divide by zero")
except:
    print('Something went wrong')
print('End')