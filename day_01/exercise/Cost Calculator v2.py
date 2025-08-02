
item_count = int(input('Enter item count: '))
total = 0

for item in range(item_count):
    item_price = int(input('Enter item price: '))
    total += item_price
print(total)