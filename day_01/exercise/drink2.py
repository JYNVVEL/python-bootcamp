def brew(drink, extra=None):

    if extra == None:
        print(f"I made you {drink}")
    else:
        print(f"I made you {drink} with {extra}")

brew('coffee', 'sugar')
brew('tea', 'milk')
brew('coffee')