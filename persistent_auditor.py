def load_orders():
    file = open("orders.txt", "a")
    file.close()
    file = open("orders.txt", "r")
    lines = file.readlines()
    file.close()
    orders = []

    for line in lines:
        order = line.split(", ")
        order_id = int(order[0])
        product_name = order[1]
        quantity = int(order[2])
        orders.append([order_id, product_name, quantity])
    return orders

def save_orders(orders):
    file = open("orders.txt", "w")
    for order in orders:
        file.write(str(order[0]) + ", " + order[1] + ", " + str(order[2]) + "\n")
    file.close()

def display_orders(orders):
    print("Current orders:\n")
    for order in orders:
        print(str(order[0]) + ", " + order[1] + ", " + str(order[2]))

def add_order(orders, product_name, quantity):
    if len(orders) == 0:
        new_id = 1001
    else:
        new_id = orders[-1][0] + 1
    new_order = [new_id, product_name, quantity]
    orders.append(new_order)
    return new_order
orders = load_orders()

while True:
    display_orders(orders)
    product_name = input("\nEnter Product Name: ")
    if product_name.lower() == "quit":
        break
    quantity = int(input("Enter Quantity: "))
    new_order = add_order(orders, product_name, quantity)
    print("\nNew Order Added:")
    print(str(new_order[0]) + ", " + new_order[1] + ", " + str(new_order[2]))
    save_orders(orders)
    print('\nOrder successfully saved to orders.txt\n')