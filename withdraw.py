def atm_withdrawal():
    # Mock account details
    stored_pin = 1234
    account_balance = 25000.0
    daily_limit = 10000.0

    print("--- Welcome to the ATM ---")
    entered_pin = int(input("Enter your 4-digit PIN: "))

    if entered_pin != stored_pin:
        print("❌ Incorrect PIN! Access Denied.")
        return

    amount = float(input("Enter amount to withdraw (₹): "))

    # Validation checks
    if amount <= 0:
        print("❌ Invalid amount. Must be greater than zero.")
    elif amount % 100 != 0:
        print("❌ Amount must be a multiple of ₹100.")
    elif amount > daily_limit:
        print(f"❌ Exceeds daily withdrawal limit of ₹{daily_limit}.")
    elif amount > account_balance:
        print("❌ Insufficient funds in your account.")
    else:
        account_balance -= amount
        print("✅ Please collect your cash.")
        print(f"💰 Remaining Account Balance: ₹{account_balance}")
atm_withdrawal()
