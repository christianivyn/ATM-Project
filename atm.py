from datetime import datetime
from pick import pick
import sys

# ---------------------------------------
# ACCOUNTS (DIRECTLY IN THE CODE)
# ---------------------------------------
accounts = {
    "Ivyn": {
        "pin": "0718",
        "balance": 5000,
        "account_number": "1234567890",
        "card_number": "521729533497",
        "cvc": "982",
        "date": "03/26"
    },

    "Sample": {
        "pin": "1234",
        "balance": 2500,
        "account_number": "9876543210",
        "card_number": "400012341234",
        "cvc": "777",
        "date": "04/28"
    }
}

# Global logged-in user
current_user_name = None
user = None


# ---------------------------------------
# GREETING
# ---------------------------------------
def greet_user(name):
    hour = datetime.now().hour

    if 5 <= hour < 12:
        greeting = "Good morning"
    elif 12 <= hour < 18:
        greeting = "Good afternoon"
    else:
        greeting = "Good evening"

    print(f"{greeting}, {name}! Access granted.\n")


# ---------------------------------------
# LOGIN USING CREDIT CARD NUMBER
# ---------------------------------------
card_input = input("Enter your credit card number (12 digits): ")

if not (card_input.isdigit() and len(card_input) == 12):
    print("Invalid credit card number format.")
    sys.exit(1)

found = False
for name, data in accounts.items():
    if data["card_number"] == card_input:
        current_user_name = name
        user = data
        found = True
        break

if not found:
    print("Credit card number not recognized. Exiting...")
    sys.exit(1)


# ---------------------------------------
# PIN CHECK
# ---------------------------------------
attempts = 0
while attempts < 3:
    pin_input = input("Enter your 4-digit PIN: ")

    if not pin_input.isdigit():
        print("PIN must be digits only.")
        sys.exit(1)

    if len(pin_input) != 4:
        print("PIN must be 4 digits.")
        attempts += 1
        continue

    if pin_input != user["pin"]:
        print("Incorrect PIN.")
        attempts += 1
        continue

    print(f"\nWelcome, {current_user_name}!\n")
    greet_user(current_user_name)
    break

if attempts == 3:
    print("Too many attempts. Access denied.")
    sys.exit(1)


# ---------------------------------------
# ATM MENU
# ---------------------------------------
def atm_menu():
    while True:
        title1 = f"Select an option:"
        title2 = f"Current Balance: ₱{user['balance']}\n{title1}\n"
        options = ["Deposit Cash", "Withdraw Cash", "Exit"]

        option, index = pick(options, title2)

        # ----------- DEPOSIT -----------
        if option == "Deposit Cash":
            amount = input("\nEnter amount to deposit: ")

            if amount.isdigit():
                amount = int(amount)
                user["balance"] += amount
                print(f"\nDeposited ₱{amount}. New Balance: ₱{user['balance']}\n")
            else:
                print("\nInvalid amount.\n")

        # ----------- WITHDRAW -----------
        elif option == "Withdraw Cash":
            amount = input("\nEnter amount to withdraw: ")

            if amount.isdigit():
                amount = int(amount)

                if amount > user["balance"]:
                    print("\nInsufficient balance.\n")
                else:
                    user["balance"] -= amount
                    print(f"\nWithdrew ₱{amount}. Remaining Balance: ₱{user['balance']}\n")
            else:
                print("\nInvalid amount.\n")

        # ----------- EXIT -----------
        elif option == "Exit":
            print("\nThank you for using the ATM. Goodbye!")
            sys.exit(0)


# ---------------------------------------
# START ATM
# ---------------------------------------
atm_menu()
