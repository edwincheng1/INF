import json
import os
from Inventory import Inventory
from PhysicalProduct import PhysicalProduct
from DigitalProduct import DigitalProduct


def load_inventory_file(filepath="inventory.json"):
    inventory = Inventory()
    if os.path.exists(filepath):
        print(f"\n{filepath} found.")
        with open(filepath, "r") as file:
            data = json.load(file)
            for item in data:
                product_type = item.get("type")
                if product_type == "digital" or str(item.get("id", "")).startswith("D"):
                    product = DigitalProduct(item["id"], item["name"], item["price"], item["stock"], item.get("download_size", 0.0))
                else:
                    product = PhysicalProduct(item["id"], item["name"], item["price"], item["stock"], item.get("weight", 0.0))
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
    print("1. Physical Product (PXXX)")
    print("2. Digital Product (DXXX)")
    choice = input("Select product type (1 or 2): ")
    if choice not in ["1", "2"]:
        print("Invalid product type.\n")
        return

    prefix = "P" if choice == "1" else "D"
    id_num = input("Product ID Number (1-999): ")
    try:
        num = int(id_num)
        if not (1 <= num <= 999):
            print("Error: ID number must be between 1 and 999.\n")
            return
        product_id = f"{prefix}{num:03d}"
    except ValueError:
        print("Error: Invalid number entered.\n")
        return

    if inventory.search_product(product_id):
        print(f"Error, Product ID {product_id} already exists\n")
        return

    print(f"Assigned Product ID: {product_id}")
    product_name = input("Product Name: ")
    price = float(input("Price: "))
    stock = int(input("Stock Quantity: "))

    if choice == "1":
        weight = float(input("Weight (kg): "))
        new_product = PhysicalProduct(product_id, product_name, price, stock, weight)
    else:
        download_size = float(input("Download Size (MB): "))
        new_product = DigitalProduct(product_id, product_name, price, stock, download_size)

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
        print("\nStock updated successfully!")
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
        if isinstance(product, PhysicalProduct):
            print(f"Weight: {product.get_weight()}kg")
            print(f"Shipping Cost: ${format(product.calculate_shipping_cost(), '.2f')}")
        elif isinstance(product, DigitalProduct):
            print(f"Download Size: {product.get_download_size()}MB")
        print(f"{product.get_fulfilment_info()}")
        print("---------------------------------------------\n")
    else:
        print("\nProduct not found\n")

def main():
    print("==============================================")
    print("INVENTORY MANAGEMENT SYSTEM")
    print("==============================================")
    inventory = load_inventory_file()
    while True:
        menu()
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

if __name__ == "__main__":
    main()
