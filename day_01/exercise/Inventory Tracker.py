import json
from textwrap import indent


def create(inventory, item):
    """Add a new item (dict) to the inventory (list[dict])"""
    inventory.append(item)

def read(inventory, index):
    """Return the item (dict) in the given index (int) of inventory"""
    if 0 <= index < len(inventory):
        return inventory[index]
    return None

def update(inventory, index, detail_key, detail_value):
    """Change/add the key and value to the given index in inventory"""
    if 0 <= index < len(inventory):
        inventory[index][detail_key] = detail_value

def delete(inventory, index):
    """Remove item (dict) in the given index (int) of inventory"""
    if 0 <= index < len(inventory):
        inventory.pop(index)

def show(inventory):
    """Print the items and their details line-by-line"""
    if not inventory:
        print("Inventory is empty.")
    for i, item in enumerate(inventory):
        print(f"{i}. {item}")

def save(inventory, filepath):
    with open(filepath, "w") as file:
        json.dump(inventory, file, indent=4)

def load(filepath):
    with open(filepath, "r") as file:
        data = json.load(file, indent=4)
        return data


def main():
    current_inventory = []
    command = input("Command (create/read/update/delete/show/exit): ")

    while command != "exit":
        if command == "create":
            name = input("Item name: ")
            quantity = input("Quantity: ")
            item = {"name": name, "Quantity": quantity}
            create(current_inventory, item)

        elif command == "read":
            index = int(input("Index: "))
            item = read(current_inventory, index)
            if item:
                print(item)
            else:
                print("Invalid index.")

        elif command == "update":
            index = int(input("Index: "))
            key = input("Field to update: ")
            value = input("New value: ")
            update(current_inventory, index, key, value)

        elif command == "delete":
            index = int(input("Index: "))
            delete(current_inventory, index)

        elif command == "show":
            show(current_inventory)

        elif command == "save":
            filepath = input("Enter filepath: ")
            save(current_inventory, filepath)

        elif command == "load":
            filepath = input("Enter filepath: ")
            current_inventory = load(filepath)

        else:
            print("Unknown command.")

        command = input("Command (create/read/update/delete/show/exit): ")


main()
