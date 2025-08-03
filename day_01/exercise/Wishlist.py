items = [
    {
        "Name : ":"Laptop",
        "Info : ":"High-End",
        "Price: ": 60_000.00
    },
    {
        "Name : ": "Smartphone",
        "Info : ": "Flagship",
        "Price: ": 37_000.00
    }
]
line = ("=" * 10)

print(f"{line} Item {line}")
for item in items:
    print("\n")
    for key, value in item.items():

        print("\t", key, value)