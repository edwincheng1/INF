import csv
import json
import os
from Supplier import Supplier
from Product import Product
from PhysicalProduct import PhysicalProduct
from DigitalProduct import DigitalProduct
from ProductFactory import ProductFactory
from Inventory import Inventory
from Order import Order
from DiscountStrategy import DiscountStrategy
from NoDiscount import NoDiscount
from PercentageDiscount import PercentageDiscount
from BulkDiscount import BulkDiscount
from StudentDiscount import StudentDiscount


DEFAULT_SUPPLIERS = [
    Supplier("S001", "Global Tech Distribution", "supply@globaltech.com"),
    Supplier("S002", "Digital Soft Distributors", "sales@digitalsoft.com"),
    Supplier("S003", "Prime Hardware Supplies", "contact@primehardware.com")
]


def get_positive_float(prompt: str) -> float:
    """Helper function that repeatedly asks for a positive float, handling exceptions gracefully."""
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                print("Please enter a number greater than zero.")
                continue
            return value
        except ValueError:
            print("Please enter a valid number, e.g. 12.50")


def load_products(path: str, inventory: Inventory, supplier: Supplier) -> None:
    """Loads products from a CSV file using try / except / else / finally and ProductFactory."""
    try:
        file = open(path, newline="")
    except FileNotFoundError:
        print(f"Products file not found: {path}")
    else:
        with file:
            reader = csv.reader(file)
            header = next(reader, None)
            loaded = 0
            for row in reader:
                if not row or len(row) < 5:
                    continue
                try:
                    p_type = row[0].strip()
                    p_id = row[1].strip()
                    name = row[2].strip()
                    price = float(row[3].strip())
                    stock = int(row[4].strip())
                    product = ProductFactory.create(p_type, p_id, name, price, stock, supplier)
                    inventory.add_product(product)
                    loaded += 1
                except ValueError as e:
                    print(f"Skipping invalid row {row}: {e}")
            print(f"{loaded} products loaded.")
    finally:
        print("Load attempt finished.")


def load_inventory_file(filepath: str = "inventory.json") -> Inventory:
    inventory = Inventory()
    if os.path.exists(filepath):
        print(f"\n{filepath} found.")
        try:
            with open(filepath, "r") as file:
                data = json.load(file)
                for item in data:
                    sup_data = item.get("supplier", {})
                    supplier = Supplier(
                        sup_data.get("supplier_id", "S001"),
                        sup_data.get("name", "Default Supplier"),
                        sup_data.get("contact_email", "supplier@inventory.com")
                    )
                    product_type = item.get("type", "physical")
                    extra = item.get("download_size", 0.0) if product_type == "digital" else item.get("weight", 0.0)
                    product = ProductFactory.create(
                        product_type, item["id"], item["name"], item["price"],
                        item["stock"], supplier, extra
                    )
                    inventory.add_product(product)
            print("Inventory loaded successfully.\n")
        except Exception as e:
            print(f"Error loading {filepath}: {e}\n")
    else:
        print(f"{filepath} not found, creating {filepath}.")
        with open(filepath, "w") as file:
            json.dump([], file, indent=4)
        print(f"{filepath} created successfully.\n")
    return inventory


def save_inventory_file(inventory: Inventory, filepath: str = "inventory.json") -> None:
    data = [p.to_dict() for p in inventory.get_all_products()]
    with open(filepath, "w") as file:
        json.dump(data, file, indent=4)


def menu() -> None:
    print("-------------MENU-------------")
    print("1. Display All Products")
    print("2. Add Product (via Factory)")
    print("3. Update Stock")
    print("4. Search Product")
    print("5. Remove Product")
    print("6. Load Products from CSV")
    print("7. Create Customer Order (with Discount Strategy)")
    print("8. Save Inventory")
    print("9. Exit")
    print("--------------------------")


def handle_add_product(inventory: Inventory) -> None:
    print("\nAdd New Product")
    print("1. Physical Product (PXXX)")
    print("2. Digital Product (DXXX)")
    choice = input("Select product type (1 or 2): ").strip()
    if choice not in ["1", "2"]:
        print("Invalid product type.\n")
        return

    product_type = "physical" if choice == "1" else "digital"
    prefix = "P" if choice == "1" else "D"
    id_num = input("Product ID Number (1-999): ").strip()
    try:
        num = int(id_num)
        if not (1 <= num <= 999):
            print("Error: ID number must be between 1 and 999.\n")
            return
        product_id = f"{prefix}{num:03d}"
    except ValueError:
        print("Error: Invalid number entered.\n")
        return

    if inventory.find_product(product_id) is not None:
        print(f"Error, Product ID {product_id} already exists\n")
        return

    print(f"Assigned Product ID: {product_id}")
    product_name = input("Product Name: ").strip()
    price = get_positive_float("Price: ")
    while True:
        try:
            stock = int(input("Stock Quantity: "))
            if stock < 0:
                print("Stock cannot be negative.")
                continue
            break
        except ValueError:
            print("Please enter a valid whole number.")

    print("\nSelect Supplier:")
    for idx, s in enumerate(DEFAULT_SUPPLIERS, 1):
        print(f"{idx}. {s.get_name()} ({s.get_supplier_id()})")
    s_choice = input("Select supplier (1-3): ").strip()
    supplier = DEFAULT_SUPPLIERS[0]
    if s_choice in ["1", "2", "3"]:
        supplier = DEFAULT_SUPPLIERS[int(s_choice) - 1]

    extra_param = 0.0
    if choice == "1":
        while True:
            try:
                extra_param = float(input("Weight (kg): "))
                if extra_param < 0:
                    print("Weight cannot be negative.")
                    continue
                break
            except ValueError:
                print("Please enter a valid number.")
    else:
        while True:
            try:
                extra_param = float(input("Download Size (MB): "))
                if extra_param < 0:
                    print("Download size cannot be negative.")
                    continue
                break
            except ValueError:
                print("Please enter a valid number.")

    try:
        new_product = ProductFactory.create(product_type, product_id, product_name, price, stock, supplier, extra_param)
        inventory.add_product(new_product)
        save_inventory_file(inventory)
        print("\nProduct added successfully via ProductFactory!\n")
    except ValueError as e:
        print(f"Validation error: {e}\n")


def handle_update_stock(inventory: Inventory) -> None:
    print("\nUpdate Stock")
    product_id = input("Enter Product ID: ").strip()
    product = inventory.find_product(product_id)
    if product is not None:
        print("\nProduct Found:")
        print(f"Name: {product.get_name()}")
        print(f"Current Stock: {product.get_stock()}")
        while True:
            try:
                new_stock = int(input("\nNew Stock Quantity: "))
                product.update_stock(new_stock)
                save_inventory_file(inventory)
                print("\nStock updated successfully!\n")
                break
            except ValueError as e:
                print(f"Invalid stock: {e}. Please enter a non-negative whole number.")
    else:
        print("\nProduct not found\n")


def handle_search_product(inventory: Inventory) -> None:
    print("\nSearch Product")
    product_id = input("Enter Product ID: ").strip()
    product = inventory.find_product(product_id)
    if product is not None:
        print("\nProduct Found")
        print("---------------------------------------------")
        print(f"ID: {product.get_product_id()}")
        print(f"Name: {product.get_name()}")
        print(f"Price: ${format(product.get_price(), '.2f')}")
        print(f"Stock: {product.get_stock()}")
        print(f"Supplier: {product.get_supplier().get_name()} ({product.get_supplier().get_contact_email()})")
        if isinstance(product, PhysicalProduct):
            print(f"Weight: {product.get_weight()}kg")
            print(f"Shipping Cost: ${format(product.calculate_shipping_cost(), '.2f')}")
        elif isinstance(product, DigitalProduct):
            print(f"Download Size: {product.get_download_size()}MB")
        print(f"Fulfilment: {product.get_fulfilment_info()}")
        print("---------------------------------------------\n")
    else:
        print("\nProduct not found\n")


def handle_remove_product(inventory: Inventory) -> None:
    print("\nRemove Product from Inventory")
    product_id = input("Enter Product ID to remove: ").strip()
    if inventory.remove_product(product_id):
        save_inventory_file(inventory)
        print(f"Product {product_id} removed from inventory successfully!\n")
    else:
        print("\nProduct not found\n")


def handle_load_csv(inventory: Inventory) -> None:
    print("\nLoad Products from CSV")
    path = input("Enter CSV filename (default 'products.csv'): ").strip()
    if not path:
        path = "products.csv"
    load_products(path, inventory, DEFAULT_SUPPLIERS[0])
    save_inventory_file(inventory)


def choose_discount_strategy() -> DiscountStrategy:
    print("\nSelect Discount Strategy:")
    print("1. No Discount")
    print("2. Percentage Discount (10%)")
    print("3. Bulk Discount ($20 off $200+)")
    print("4. Student Discount (5%)")
    choice = input("Enter choice (1-4, default 1): ").strip()
    if choice == "2":
        return PercentageDiscount(10.0)
    elif choice == "3":
        return BulkDiscount(200.0, 20.0)
    elif choice == "4":
        return StudentDiscount(5.0)
    else:
        return NoDiscount()


def handle_create_order(inventory: Inventory) -> None:
    print("\nCreate Customer Order")
    order_id = input("Enter Order ID (e.g. ORD101): ").strip()
    if not order_id:
        print("Order ID cannot be empty.\n")
        return

    discount_strategy = choose_discount_strategy()
    order = Order(order_id, discount_strategy)

    while True:
        pid = input("Enter Product ID to add to order (or 'done' to finish): ").strip()
        if pid.lower() == "done":
            break
        product = inventory.find_product(pid)
        if product is None:
            print("Product not found in inventory.\n")
            continue

        current_order_qty = sum(line.quantity for line in order.order_lines if line.product.get_product_id().upper() == product.get_product_id().upper())
        available_stock = product.get_stock() - current_order_qty

        if available_stock <= 0:
            print(f"Error: {product.get_name()} ({product.get_product_id()}) has no available stock remaining.\n")
            continue

        try:
            qty = int(input(f"Enter quantity for {product.get_name()} (Available stock: {available_stock}): "))
            if qty <= 0:
                print("Quantity must be greater than zero.\n")
                continue
            if qty > available_stock:
                print(f"Error: Requested quantity ({qty}) exceeds available stock ({available_stock}).\n")
                continue

            order.add_order_line(product, qty)
            print(f"Added {qty}x {product.get_name()} to order.\n")
        except ValueError as e:
            print(f"Validation error: {e}. Please enter a valid whole number.\n")

    if not order.order_lines:
        print("Order is empty. Order creation cancelled.\n")
        return

    order.display_order()

    # Deduct stock
    for line in order.order_lines:
        new_stock = line.product.get_stock() - line.quantity
        line.product.update_stock(new_stock)

    save_inventory_file(inventory)
    print("Order placed successfully! Stock levels have been deducted and saved.\n")


def main() -> None:
    print("==============================================")
    print("INVENTORY MANAGEMENT SYSTEM (LAB 9)")
    print("==============================================")
    inventory = load_inventory_file()
    while True:
        menu()
        option = input("Enter option: ").strip()
        if option == "1":
            inventory.display_all()
        elif option == "2":
            handle_add_product(inventory)
        elif option == "3":
            handle_update_stock(inventory)
        elif option == "4":
            handle_search_product(inventory)
        elif option == "5":
            handle_remove_product(inventory)
        elif option == "6":
            handle_load_csv(inventory)
        elif option == "7":
            handle_create_order(inventory)
        elif option == "8":
            print("\nSaving Inventory...")
            save_inventory_file(inventory)
            print("Inventory saved successfully to inventory.json\n")
        elif option == "9":
            print("\nSaving inventory before exit...")
            save_inventory_file(inventory)
            print("Inventory saved successfully.")
            print("\nThank you for using Inventory Management System.\nProgram terminated.\n")
            break
        else:
            print("\nError. Please enter option 1 to 9.\n")


if __name__ == "__main__":
    main()
