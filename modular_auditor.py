stock = 0
failed = 0
deliveries = 0

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

while True:
    stockinput = get_valid_input()
    if stockinput == "quit":
        generate_report(stock, failed)
        break
    elif stockinput == "Invalid":
        print("Invalid input. Please enter a positive number.")
        failed += 1

    else:
        stock = process_delivery(stock, stockinput)
        tax = calculate_tax(stockinput)
        deliveries = deliveries + 1
        if stock > 0:
            print("Number of deliveries processed:", deliveries)
            print("Tax:",calculate_tax(stockinput))