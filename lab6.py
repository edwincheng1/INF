import json
import os


class Product:
    def __init__(self, product_id, name, price, stock):
        self._product_id = product_id
        self._name = name
        self._price = price
        self._stock = stock

    def get_product_id(self):
        return self._product_id

    def get_name(self):
        return self._name

    def get_price(self):
        return self._price

    def get_stock(self):
        return self._stock

    def update_stock(self, quantity):
        self._stock = quantity

    def display_information(self):
        print(f"ID: {self._product_id} | Name: {self._name} | Price: ${format(self._price, '.2f')} | Stock: {self._stock}")

    def to_dict(self):
        return {"id": self._product_id,"name": self._name,"price": self._price,"stock": self._stock}

class Inventory:
    def __init__(self):
        self._products = []

    def add_product(self, product):
        self._products.append(product)

    def search_product(self, product_id):
        for product in self._products:
            if product.get_product_id() == product_id:
                return product

    def display_all(self):
        print("\nCurrent Inventory")
        print("---------------------------------------------")
        if not self._products:
            print("Inventory is empty.")
        else:
            for product in self._products:
                product.display_information()
        print("---------------------------------------------\n")

    def get_all_products(self):
        return self._products

def load_inventory_file(filepath="inventory.json"):
    inventory = Inventory()
    if os.path.exists(filepath):
        print(f"\n{filepath} found.")
        with open(filepath, "r") as file:
            data = json.load(file)
            for item in data:
                product = Product(item["id"], item["name"], item["price"], item["stock"])
                inventory.add_product(product)
        print("Inventory loaded successfully.\n")
    else:
        print(f"{filepath} not found, creating {filepath}.")
        with open(filepath, "w") as file:
            json.dump([], file, indent=4)
        print(f"{filepath} created successfully.\n")
    return inventory

def save_inventory_file(inventory, filepath="inventory.json"):
    data = [p.to_dict() for p in inventory.get_all_products()]
    with open(filepath, "w") as file:
        json.dump(data, file, indent=4)

def menu():
    print("-------------MENU-------------")
    print("1. Display All Products")
    print("2. Add Product")
    print("3. Update Stock")
    print("4. Search Product")
    print("5. Save Inventory")
    print("6. Exit")
    print("--------------------------")

def handle_add_product(inventory):
    print("\nAdd New Product")
    product_id = input("Product ID: ")
    if inventory.search_product(product_id):
        print("Error, Product ID already exists\n")
        return

    product_name = input("Product Name: ")
    price = float(input("Price: "))
    stock = int(input("Stock Quantity: "))
    new_product = Product(product_id, product_name, price, stock)
    inventory.add_product(new_product)
    save_inventory_file(inventory)
    print("\nProduct added successfully!\n")

def handle_update_stock(inventory):
    print("\nUpdate Stock")
    product_id = input("Enter Product ID: ")
    product = inventory.search_product(product_id)
    if product:
        print("\nProduct Found:")
        print(f"Name: {product.get_name()}")
        print(f"Current Stock: {product.get_stock()}")
        new_stock = int(input("\nNew Stock Quantity: "))
        product.update_stock(new_stock)
        save_inventory_file(inventory)
        print("\nStock updated successfully!\n")
    else:
        print("\nProduct not found\n")

def handle_search_product(inventory):
    print("\nSearch Product")
    product_id = input("Enter Product ID: ")
    product = inventory.search_product(product_id)
    if product:
        print("\nProduct Found")
        print("---------------------------------------------")
        print(f"ID: {product.get_product_id()}")
        print(f"Name: {product.get_name()}")
        print(f"Price: ${format(product.get_price(), '.2f')}")
        print(f"Stock: {product.get_stock()}")
        print("---------------------------------------------\\n")
    else:
        print("\nProduct not found\n")

def main():
    print("==============================================")
    print("INVENTORY MANAGEMENT SYSTEM")
    print("==============================================")
    inventory = load_inventory_file()
    menu()
    while True:
        option = input("Enter option: ")
        if option == "1":
            inventory.display_all()
        elif option == "2":
            handle_add_product(inventory)
        elif option == "3":
            handle_update_stock(inventory)
        elif option == "4":
            handle_search_product(inventory)
        elif option == "5":
            print("\nSaving Inventory...")
            save_inventory_file(inventory)
            print("Inventory saved successfully to inventory.json\n")
        elif option == "6":
            print("\nSaving inventory before exit...")
            save_inventory_file(inventory)
            print("Inventory saved successfully.")
            print("\nThank you for using Inventory Management System.\nProgram terminated.\n")
            break
        else:
            print("\nError. Please enter option 1 to 6.\n")

print('')

if __name__ == "__main__":
    main()