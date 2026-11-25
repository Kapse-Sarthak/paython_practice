def calculate_electricity_bill(units):
    bill = 0.0
    fixed_charge = 50.0

    if units <= 100:
        bill = units * 1.50
    elif units <= 200:
        bill = (100 * 1.50) + ((units - 100) * 2.50)
    elif units <= 300:
        bill = (100 * 1.50) + (100 * 2.50) + ((units - 200) * 4.00)
    else:
        bill = (100 * 1.50) + (100 * 2.50) + (100 * 4.00) + ((units - 300) * 5.00)

    total_bill = bill + fixed_charge
    return total_bill

# Main execution
units_consumed = float(input("Enter total electricity units consumed: "))

if units_consumed < 0:
    print("Invalid input! Units cannot be negative.")
else:
    amount = calculate_electricity_bill(units_consumed)
    print(f"Total Electricity Bill: ₹{amount:.2f}")