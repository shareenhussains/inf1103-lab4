def get_valid_input():
    stock = input("Enter stock quantity (or 'quit' to exit): ")

    if stock.lower() == "quit":
        return "quit"

    if not stock.isdigit():
        print("Invalid input. Please enter a whole number.")
        return "invalid"

    return int(stock)

def process_delivery(current_total, new_value):
    new_total = current_total + new_value
    return new_total

def calculate_tax(amount):
    tax = amount * 0.10
    return tax

def generate_report(total_units, failed_attempts):
    print("Total Units Processed:", total_units)
    print("Number of Failed/Rejected Entries:", failed_attempts)


inventory = 0
failed_entries = 0
deliveries_processed = 0

while True:
    stock = get_valid_input()

    if stock == "quit":
        break

    if stock == "invalid":
        failed_entries += 1
        continue

    inventory = process_delivery(inventory, stock)

    tax = calculate_tax(stock)

    print("Tax for this delivery:", tax)
    print("Current inventory:", inventory)

    deliveries_processed += 1

    if inventory > 500:
        print("ALERT: Overstock! Inventory exceeds 500 units.")
        break

generate_report(deliveries_processed, failed_entries)