prices = [1_000, 10, 200, 1000, 3_000]

discounted_prices = []

for price in prices:
    discounted_prices.append(price / 2)

print(discounted_prices)

discounted_prices = [price / 2 for price in prices]

print(discounted_prices)