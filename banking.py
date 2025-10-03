# Group 3 - Joshua Hartneck and Rachel Kristofferson
# CSC330 100 - Language Design and Implementation
# Final Group Project - Fall 2025
#

from bank_account import BankAccount
from lexer import Lexer
from ast_node import ASTNode
from interpreter import Interpreter
from parser import Parser
from token import Token

# NEED TO IMPLEMENT
# create_account, change_account, login_to_account, find_account

# Constants
ACCOUNTS = []
EXIT_KEYWORDS = ["exit", "quit", "end", "logout"]



##############################
#### Initialize Accounts  ####
##############################
def initialize_accounts():
    """Initializes a list of 10 bank accounts.
       Firstname, lastname, account number, account balance"""
    
    bank_accounts = [
        ("Rachel", "Kristofferson", "RK123456", 1000.00),
        ("Joshua", "Hartneck", "JH234567", 10000.50),
        ("Bryce", "Beeskow", "BB345678", 345.70),
        ("Zachary", "Christianson", "ZC456789", 3334.06),
        ("Asia", "Elmi", "AE567890", 100.00),
        ("Jonas", "Frahm", "JF654321", 1.08),
        ("Dan", "Obermiller", "DO765432", 10000.70),
        ("Tyson", "Radke", "TR876543", 777.07),
        ("Thomas", "Sauro", "TS987654", 43.07),
        ("Moua", "Yang", "MY098765", 246.09),
    ]
        
    # Populate global constant ACCOUNTS with bank accounts
    for first, last, account_num, account_bal in bank_accounts:
        account = BankAccount(first, last, account_num, account_bal)
        ACCOUNTS.append(account)



##############################
####     Account Menu     ####
##############################
def account_menu(account):
    """Menu once logged into account"""

    logged_in = True

    while logged_in:
        print(f"Welcome, {account.get_first_name()} {account.get_last_name()}")
        print(f"Account Number:  {account.get_account_number()}")
        print("1. Make a deposit")
        print("2. Make a withdrawal")
        print("3. Check balance")
        print("4. Logout")

        choice = input("Enter your choice (1-4) or 'Logout'").strip().lower()

        if choice == "1":
            deposit(account)
            logged_in = logout_or_continue(account)
        elif choice == "2":
            withdraw(account)
            logged_in = logout_or_continue(account)
        elif choice == "3":
            check_balance(account)
            logged_in = logout_or_continue(account)
        elif choice == "4":
            logged_in = False
        else:
            print("Invalid choice. Please select 1-4")



##############################
#### Display All Accounts ####
##############################
def display_all_accounts():
    """Displays all accounts in the ACCOUNTS list"""

    print("\t\tAll Accounts")
    print(f"{"Account Number: "} {"Name: "} {"Balance: "}")
    
    for account in ACCOUNTS:
        name = f"{account.get_first_name()} {account.get_last_name()}"
        balance = f"${account.get_balance():,.2f}"
        print(f"{account.get_account_number()} {name} {balance}")



##############################
####     Check Balance    ####
##############################
def check_balance(account):
    """Checks balance of an account"""

    print("Check balance")
    print(f"Account Holder: {account.get_first_name()} {account.get_last_name()}")
    print(f"Account number: {account.get_account_number()}")
    print(f"Current balance: {account.get_balance():.2f}")



##############################
####  Logout or Continue  ####
##############################
def logout_or_continue(account):
    """Asks the user if they'd like to continue on or logout of their account"""

    continue_on = input("Would you like another option, or logout? (continue/logout)").strip().lower()

    if continue_on == "logout":
        print(f"Loggout out of account {account.get_account_number()}")
        return False
    else:
        return True


##############################
####        Deposit       ####
##############################
def deposit(account):
    """Deposits money into a user's account"""

    print("Make a deposit")
    deposit_amount = input("Enter amount to deposit: $").strip()

    try:
        amount = float(deposit_amount)

        if amount <= 0:
            print("Error: Must be value larger than 0")
            return
        success = account.deposit(amount)

        if success:
            print(f"Successfully deposited ${amount:.2f}")
            print(f"New balance: ${account.get_balance():.2f}")
        else:
            print("Error: Deposit failed")
    
    except ValueError:
        print("Error - Invalid Input: Please enter in a number")

##############################
####        Withdraw      ####
##############################
def withdraw(account):
    """Withdrawals money from a user's account"""

    print("Make a withdrawal")
    withdrawal_amount = input("Enter an amount to withdraw: $").strip()

    try:
        amount = float(withdrawal_amount)
        if amount <= 0:
            print("Error: Must be value larger than 0")
            return
        
        success = account.withdraw(amount)

        if success:
            print(f"Successfully withdrew ${amount:.2f}")
            print(f"New balance: ${account.get_balance():.2f}")
        else:
            print("Error: Withdrawal failed")
    
    except ValueError:
        print("Error - Invalid Input: Please enter in a number")
                  

##############################
####         Main         ####
##############################
def main():
    """Main program of the banking program"""

    print("Welcome to the Bank")

    initialize_accounts()

    running = True
    while running:
        print("Main Menu")
        print("1. Access an existing account")
        print("2. Create a new account")
        print("3. View all accounts")
        print("4. Exit")

        choice = input("enter your choice (1-4) or type 'exit").strip().lower()

        if choice == "1":
            access_account()

            # Ask after logout from first account
            check_another_acc = input("Would you like to check another account? (yes/no): ").strip().lower()
            if check_another_acc == "yes" or check_another_acc == "y":
                access_account()
        elif choice == "2":
            create_account()
        elif choice == "3":
            display_all_accounts()
        elif choice == "4":
            running = False
            print("Thank you!\nGoodbye!")
        else:
            print("Invalid choice. Please select 1-4 or type 'exit'")

if __name__ == "__main__":
    main()

