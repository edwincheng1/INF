stock = 0
failed = 0
while True:
    stockinput = input("Input stock quantity or type 'quit': ")
    if stockinput.lower() == "quit":
        print("Total Units Processed:", stock)
        print("Number of Failed/Rejected Entries:", failed)
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
        if stock > 500:
            print("Total inventory is more than 500. End of program.")
            break
        else:
            print("Total inventory stock:", stock)