import time

# ================================
# INITIAL SETUP
# ================================
PASSWORD = 2004
balance = 5000
transaction_history = []

print("Welcome to ATM System")
time.sleep(1)

# ================================
# PIN VERIFICATION (3 Attempts)
# ================================
attempts = 3

while attempts > 0:
    try:
        pin = int(input("Enter your PIN: "))
    except ValueError:
        print("Invalid input. Enter numbers only.")
        continue

    if pin == PASSWORD:
        print("Login successful!\n")
        break
    else:
        attempts -= 1
        print(f"Wrong PIN. Attempts left: {attempts}")

if attempts == 0:
    print("Too many failed attempts. Account blocked.")
    exit()

# ================================
# MAIN MENU
# ================================
while True:
    print("""
===== ATM MENU =====
1. Check Balance
2. Withdraw
3. Deposit
4. Transaction History
5. Exit
""")

    try:
        option = int(input("Enter your choice: "))
    except ValueError:
        print("Please enter a valid number.")
        continue

    # ================================
    # CHECK BALANCE
    # ================================
    if option == 1:
        print(f"💰 Current Balance: ₹{balance}")

    # ================================
    # WITHDRAW
    # ================================
    elif option == 2:
        try:
            amount = int(input("Enter withdrawal amount: "))
        except ValueError:
            print("Invalid amount.")
            continue

        if amount <= 0:
            print("Amount must be greater than 0.")
        elif amount > balance:
            print("❌ Insufficient funds.")
        else:
            balance -= amount
            print(f"✅ ₹{amount} withdrawn successfully.")
            print(f"Updated Balance: ₹{balance}")
            transaction_history.append(f"Withdraw: ₹{amount} | Balance: ₹{balance}")

    # ================================
    # DEPOSIT
    # ================================
    elif option == 3:
        try:
            amount = int(input("Enter deposit amount: "))
        except ValueError:
            print("Invalid amount.")
            continue

        if amount <= 0:
            print("Amount must be greater than 0.")
        else:
            balance += amount
            print(f"✅ ₹{amount} deposited successfully.")
            print(f"Updated Balance: ₹{balance}")
            transaction_history.append(f"Deposit: ₹{amount} | Balance: ₹{balance}")

    # ================================
    # TRANSACTION HISTORY
    # ================================
    elif option == 4:
        if not transaction_history:
            print("No transactions yet.")
        else:
            print("\n--- Transaction History ---")
            for t in transaction_history:
                print(t)

    # ================================
    # EXIT
    # ================================
    elif option == 5:
        print("Thank you for using ATM. Goodbye!")
        break

    else:
        print("Invalid option. Try again.")
