import json
import os

def menu():
    print('-------------MENU-------------')
    print('1. Display All Products')
    print('2. Add Product')
    print('3. Update Stock')
    print('4. Search Product')
    print('5. Save Inventory')
    print('6. Exit')
    print('--------------------------')

def load_inventory():
    if os.path.exists("inventory.json"):
        print("\ninventory.json found")
        file = open("inventory.json","r")
        inventory = json.load(file)
        file.close()
        
        print('Inventory loaded successfully\n')
        return inventory
    
    else:
        print('inventory.json not found, creating inventory.json.')
        inventory = []
        file = open('inventory.json','w')
        json.dump(inventory, file, indent=4)
        file.close()
        print('inventory.json created succcessfully.')
        return inventory

def save_inventory(inventory):
    file = open('inventory.json','w')
    json.dump(inventory, file,indent=4)
    file.close()

def display_all(inventory):
    print('\nCurrent Inventory')
    print('---------------------------------------------')

    if len(inventory) == 0:
        print('Inventory is empty.')

    else:
        for product in inventory:
            print("ID: " + product['id'] + "| Name: " + product['name'] + '| Price: $' + 
                  format(product['price'], '.2f') + "| Stock: " + str(product['stock']))
    print('---------------------------------------------\n')

def add_product(inventory):
    print('\nAdd New Product')
    product_id = input('Product ID: ')
    for product in inventory:
        if product['id'] == product_id:
            print('Error, Product ID already exists')
            return

    product_name = input('Product Name: ')
    price = float(input('Price: '))
    stock = int(input('Stock Quantity: '))

    new_product = {'id': product_id, 'name': product_name, 'price': price, 'stock': stock}
    inventory.append(new_product)
    save_inventory(inventory)
    print('\nProduct added successfully!\n')

def update_stock(inventory):
    print('\nUpdate Stock')
    product_id = input('Enter Product ID: ')

    for product in inventory:
        if product['id'] == product_id:
            print('\nProduct Found:')
            print('Name: ' + product['name'])
            print('Current Stock: ' + str(product['stock']))

            new_stock = int(input('\nNew Stock Quantity: '))
            product['stock'] = new_stock
            save_inventory(inventory)
            print('\nStock updated successfully!\n')
            return
    print('\nProduct not found\n')

def search_product(inventory):
    print('Search Product')
    product_id = input('Enter Product ID: ')
    for product in inventory:
        if product['id'] == product_id:
            print('\nProduct Found')
            print('---------------------------------------------')
            print('ID: ' + product['id'])
            print('Name: ' + product['name'])
            print('Price: '+ format(product['price'], '.2f'))
            print('Stock: '+ str(product['stock']))
            print('---------------------------------------------\n')
            return
    print('\nProduct not found\n')

def main():
    print('==============================================')
    print('INVENTORY MANAGEMENT SYSTEM')
    print('==============================================')
    inventory = load_inventory()
    menu()

    while True:
        option = input('Enter option: ')

        if option == '1':
            display_all(inventory)

        elif option == '2':
            add_product(inventory)

        elif option == '3':
            update_stock(inventory)

        elif option == '4':
            search_product(inventory)

        elif option == '5':
            print('\nSaving Inventory...')
            save_inventory(inventory)
            print('Inventory saved successfully to inventory.json\n')

        elif option == '6':
            print('\nSaving inventory before exit...')
            save_inventory(inventory)
            print('Inventory saved successfully.')
            print('\nThank you for using Inventory Management System.\nProgram terminated.\n')
            break

        else:
            print('\nError. Please enter option 1 to 6.\n')

main()