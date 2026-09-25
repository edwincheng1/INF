stock = 0
failed = 0
deliveries = 0
transaction_history = []

def load_inventory():
    file = open("inventory.txt", "a")
    file.close()
    file = open("inventory.txt", "r")
    lines = file.readlines()
    file.close()

    if len(lines) == 0:
        return 0, []

    total_stock = int(lines[0])
    history = []

    if len(lines) > 1:
        history_lines = lines[1]
        if history_lines != "":
            history = history_lines.split(",")

            for i in range(len(history)):
                history[i] = int(history[i])

    return total_stock, history

def save_inventory(total_stock, history):
    file = open("inventory.txt", "w")
    file.write(str(total_stock) + "\n")
    for i in range(len(history)):
        file.write(str(history[i]))

        if i < len(history) - 1:
            file.write(",")

    file.close()
    print("Inventory successfully saved to inventory.txt")


def get_valid_input():
    stockinput = input("Input stock quantity or type 'quit': ")
    if stockinput.lower() == "quit":
        return "quit"
    elif stockinput.startswith("-"):
        print("Invalid input. Please enter a positive number.")
        return "Invalid"
    elif not stockinput.isdigit():
        print("Invalid input. Please enter an integer.")
        return "Invalid"
    else:
        return int(stockinput)

def process_delivery(current_total, new_value):
    new_value = new_value + current_total
    return new_value

def calculate_tax(amount):
    tax = amount * 0.1
    tax = f"{tax:.2f}"
    return tax

def generate_report(total_units, failed_attempts):
    print("Total Deliveries Processed:", total_units)
    print("Number of Failed/Rejected Entries:", failed_attempts)

stock, transaction_history = load_inventory()
deliveries = len(transaction_history)

print("Current Inventory:", stock)
print("Transaction History:", transaction_history)

while True:
    stockinput = get_valid_input()
    if stockinput == "quit":
        save_inventory(stock, transaction_history)
        generate_report(deliveries, failed)
        break
    elif stockinput == "Invalid":
        failed += 1

    else:
        stock = process_delivery(stock, stockinput)
        transaction_history.append(stockinput)
        deliveries = deliveries + 1
        print("Number of deliveries processed:", deliveries)
        print("Tax:", calculate_tax(stockinput))
        print("Current Inventory:", stock)