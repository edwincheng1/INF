stock = 0
failed = 0

def get_valid_input():
    p = 1

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
    stockinput = input("Input stock quantity or type 'quit': ")
    if stockinput.lower() == "quit":
        generate_report(stock, failed)
        break
    elif stockinput.startswith("-"):
        print("Invalid input. Please enter a positive number.")
        failed += 1
    elif not stockinput.isdigit():
        print("Invalid input. Please enter an integer.")
        failed += 1
    else:
        stockcount = int(stockinput)
        stock = stock + stockcount
        calculate_tax(stockcount)
        if stock > 0:
            print("Number of deliveries processed:", stock)
            print("Tax:",calculate_tax(stockcount))