
for item in range(100):
    skip = item >= 20 and item <= 80
    if skip:
        continue
    print(item)