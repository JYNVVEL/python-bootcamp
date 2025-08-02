item_1_price = float(input("Item 1: "))
item_2_price = float(input("Item 2: "))
item_3_price = float(input("Item 3: "))

total = item_3_price + item_2_price + item_3_price
print(f"First Item: ${item_1_price} \nSecond Item: ${item_2_price} \nThird Item: ${item_3_price}")
print(f"Total: ${total:.2f}")