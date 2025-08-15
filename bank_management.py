import os

Accounts = "accounts.txt"

if not os.path.exists(Accounts):
    with open(Accounts, "w") as f:
        pass




def create_account(accounts):
    name = input("Enter your name: ")
    account_number = input("Enter account number: ")
    balance = float(input("Enter initial deposit amount: "))
    
    with open(accounts, "a") as file:
        file.write(f"{name},{account_number},{balance}\n")
    
    print("Account created successfully!\n")


def deposit_money(accounts):
    account_number = input("Enter your account number: ")
    amount = float(input("Enter amount to deposit: "))
    updated = False
    lines = []

    with open(accounts, "r") as file:
        lines = file.readlines()
    
    with open(accounts, "w") as file:
        for line in lines:
            name, acc_num, balance = line.strip().split(',')
            if acc_num == account_number:
                balance = float(balance) + amount
                updated = True
            file.write(f"{name},{acc_num},{balance}\n")
    
    print("Deposit successful!" if updated else "Account not found!")


def withdraw_money(accounts):
    account_number = input("Enter your account number: ")
    amount = float(input("Enter amount to withdraw: "))
    updated = False
    lines = []

    with open(accounts, "r") as file:
        lines = file.readlines()

    with open(accounts, "w") as file:
        for line in lines:
            name, acc_num, balance = line.strip().split(',')
            balance = float(balance)
            if acc_num == account_number:
                if balance >= amount:
                    balance -= amount
                    updated = True
                else:
                    print("Insufficient balance!")
            file.write(f"{name},{acc_num},{balance}\n")
    
    print("Withdrawal successful!" if updated else "Account not found or insufficient balance!")


def check_balance(accounts):
    account_number = input("Enter your account number: ")

    with open(accounts, "r") as file:
        for line in file:
            name, acc_num, balance = line.strip().split(',')
            if acc_num == account_number:
                print(f"Account Holder: {name}, Balance: {balance}")
                return
    print("Account not found!")


def delete_account(accounts):
    account_number = input("Enter your account number to delete: ")
    updated = False
    lines = []

    with open(accounts, "r") as file:
        lines = file.readlines()

    with open(accounts, "w") as file:
        for line in lines:
            name, acc_num, balance = line.strip().split(',')
            if acc_num != account_number:
                file.write(line)
            else:
                updated = True

    print("Account deleted successfully!" if updated else "Account not found!")

while True:
    print("\n===== Welcome to the Bank Management System =====")
    print("1. Create Account")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Check Balance")
    print("5. Delete Account")
    print("6. Exit")
    
    choice = input("Enter your choice: ").strip()

    if choice == "1":
        create_account(Accounts)
    elif choice == "2":
        deposit_money(Accounts)
    elif choice == "3":
        withdraw_money(Accounts)
    elif choice == "4":
        check_balance(Accounts)
    elif choice == "5":
        delete_account(Accounts)
    elif choice == "6":
        print("Thank you for using the Bank Management System!")
        break
    else:
        print("Invalid choice, please try again.")
