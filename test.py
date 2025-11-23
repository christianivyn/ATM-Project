import tkinter as tk
from tkinter import messagebox

# ---------------------------------------
# ACCOUNTS
# ---------------------------------------
accounts = {
    "Ivyn": {
        "pin": "0718",
        "balance": 5000,
        "card_number": "5217295393293497"
    },

    "Sample": {
        "pin": "1234",
        "balance": 2500,
        "card_number": "5217295388182432"
    }
}

current_user = None


# ---------------------------------------
# LOGIN FUNCTION
# ---------------------------------------
def login():
    global current_user

    card = entry_card.get()
    pin = entry_pin.get()

    # Validate card number
    for name, data in accounts.items():
        if data["card_number"] == card:
            if data["pin"] == pin:
                current_user = data
                open_atm_window(name)
                return
            else:
                messagebox.showerror("Error", "Incorrect PIN")
                return

    messagebox.showerror("Error", "Card number not recognized")


# ---------------------------------------
# ATM MENU WINDOW
# ---------------------------------------
def open_atm_window(name):
    login_window.destroy()

    atm = tk.Tk()
    atm.title("ATM Machine")
    atm.geometry("300x300")

    tk.Label(atm, text=f"Welcome, {name}!", font=("Arial", 14)).pack(pady=10)

    # ---- Buttons ----
    tk.Button(atm, text="Check Balance", width=18, command=check_balance).pack(pady=5)
    tk.Button(atm, text="Deposit Cash", width=18, command=deposit).pack(pady=5)
    tk.Button(atm, text="Withdraw Cash", width=18, command=withdraw).pack(pady=5)
    tk.Button(atm, text="Exit", width=18, command=atm.quit).pack(pady=20)

    atm.mainloop()


# ---------------------------------------
# CHECK BALANCE
# ---------------------------------------
def check_balance():
    messagebox.showinfo("Balance", f"Your balance is ₱{current_user['balance']}")


# ---------------------------------------
# DEPOSIT
# ---------------------------------------
def deposit():
    amount = simple_prompt("Enter amount to deposit:")

    if amount is None:
        return

    if not amount.isdigit():
        messagebox.showerror("Error", "Invalid amount")
        return

    current_user["balance"] += int(amount)
    messagebox.showinfo("Success", f"Deposited ₱{amount}\nNew Balance: ₱{current_user['balance']}")


# ---------------------------------------
# WITHDRAW
# ---------------------------------------
def withdraw():
    amount = simple_prompt("Enter amount to withdraw:")

    if amount is None:
        return

    if not amount.isdigit():
        messagebox.showerror("Error", "Invalid amount")
        return

    amount = int(amount)

    if amount > current_user["balance"]:
        messagebox.showerror("Error", "Insufficient balance")
        return

    current_user["balance"] -= amount
    messagebox.showinfo("Success", f"Withdrew ₱{amount}\nRemaining Balance: ₱{current_user['balance']}")


# ---------------------------------------
# SIMPLE POPUP INPUT
# ---------------------------------------
def simple_prompt(message):
    popup = tk.Toplevel()
    popup.title("Input")
    popup.geometry("250x120")

    tk.Label(popup, text=message).pack(pady=5)
    entry = tk.Entry(popup)
    entry.pack(pady=5)

    result = {"value": None}

    def submit():
        result["value"] = entry.get()
        popup.destroy()

    tk.Button(popup, text="Submit", command=submit).pack(pady=5)

    popup.grab_set()
    popup.wait_window()

    return result["value"]


# ---------------------------------------
# LOGIN WINDOW GUI
# ---------------------------------------
login_window = tk.Tk()
login_window.title("ATM Login")
login_window.geometry("300x200")

tk.Label(login_window, text="Credit Card Number:").pack(pady=5)
entry_card = tk.Entry(login_window)
entry_card.pack()

tk.Label(login_window, text="PIN:").pack(pady=5)
entry_pin = tk.Entry(login_window, show="*")
entry_pin.pack()

tk.Button(login_window, text="Login", command=login).pack(pady=20)

login_window.mainloop()
