import json

inventory_file = "inventory.json"
sales_file = "sales.json"

def load_inventory():
    try:
        with open(inventory_file) as file:
            inventory = json.load(file)
    except FileNotFoundError:
        inventory = {}
    
    return inventory

def save_inventory(inventory):
    with open(inventory_file, "w") as file:
        json.dump(inventory, file)

def load_sales():
    try:
        with open(sales_file) as file:
            sales = json.load(file)
    except FileNotFoundError:
        sales = []
    
    return sales

def save_sales(sales):
    with open(sales_file, "w") as file:
        json.dump(sales, file)

def add_snack(inventory, snack_id, snack_name, price):
    if snack_id in inventory:
        print("Snack with the same ID already exists.")
        return

    inventory[snack_id] = {
        "name": snack_name,
        "price": price,
        "available": True
    }
    
    save_inventory(inventory)
    print(f"Snack {snack_name} added to the inventory.")

def remove_snack(inventory, snack_id):
    if snack_id not in inventory:
        print("Snack not found in inventory.")
        return

    del inventory[snack_id]
    
    save_inventory(inventory)
    print("Snack removed from the inventory.")

def update_snack_availability(inventory, snack_id, available):
    if snack_id not in inventory:
        print("Snack not found in inventory.")
        return

    inventory[snack_id]["available"] = available
    
    save_inventory(inventory)
    print("Snack availability updated.")

def sell_snack(inventory, sales, snack_id):
    if snack_id not in inventory:
        print("Snack not found in inventory.")
        return

    snack = inventory[snack_id]
    if not snack["available"]:
        print("Snack is not available for sale.")
        return

    inventory[snack_id]["available"] = False
    sale = {
        "snack_id": snack_id,
        "name": snack["name"],
        "price": snack["price"]
    }
    sales.append(sale)

    save_inventory(inventory)
    save_sales(sales)
    print(f"Snack {snack['name']} sold.")

def display_inventory(inventory):
    print("Current Inventory:")
    for snack_id, snack_data in inventory.items():
        snack_name = snack_data["name"]
        price = snack_data["price"]
        available = "Yes" if snack_data["available"] else "No"
        print(f"ID: {snack_id}, Name: {snack_name}, Price: {price}, Available: {available}")

def display_sales(sales):
    print("Sales History:")
    total_revenue = 0
    for sale in sales:
        snack_id = sale["snack_id"]
        snack_name = sale["name"]
        price = sale["price"]
        total_revenue += price
        print(f"ID: {snack_id}, Name: {snack_name}, Price: {price}")
    print(f"Total Revenue: ${total_revenue}")

def main():
    inventory = load_inventory()
    sales = load_sales()

    while True:
        print("=== Canteen Snack Inventory ===")
        print("1. Add Snack to Inventory")
        print("2. Remove Snack from Inventory")
        print("3. Update Snack Availability")
        print("4. Sell Snack")
        print("5. Display Inventory")
        print("6. Display Sales")
        print("7. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            snack_id = input("Enter snack ID: ")
            snack_name = input("Enter snack name: ")
            price = float(input("Enter price: "))
            add_snack(inventory, snack_id, snack_name, price)
        elif choice == "2":
            snack_id = input("Enter snack ID: ")
            remove_snack(inventory, snack_id)
        elif choice == "3":
            snack_id = input("Enter snack ID: ")
            available = input("Is snack available? (yes/no): ").lower() == "yes"
            update_snack_availability(inventory, snack_id, available)
        elif choice == "4":
            snack_id = input("Enter snack ID: ")
            sell_snack(inventory, sales, snack_id)
        elif choice == "5":
            display_inventory(inventory)
        elif choice == "6":
            display_sales(sales)
        elif choice == "7":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
