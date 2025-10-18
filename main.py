
import BankAccount


menu = """
****************************
1- Add a new account
2- Deposit Money
3- Withdraw Money
4- Check Balance
5- Show all accounts
6- exit
****************************
"""
def add_new_account(accounts):
    '''
    first it will check if account holder is exists or not
    if exists -> print a message
    if not it will add new account with checking the initial balnce is more than or eqal to 0
    '''
    try:
        name = input("Please Enter name of Account holder : ").strip()
        if not name:
            raise ValueError("Account holder name cannot be empty!")
        
        name_exists = any(acc.get_account_holder().lower() == name.lower() for acc in accounts)
        if name_exists:
            print("The name already exists, please add a new person!")
            return  
        while True:
            initial_balance = input("Please Enter initial balance of the account : ").strip()
            try:
                initial_balance = float(initial_balance)
                if initial_balance < 0:
                    raise ValueError("Initial balance cannot be negative!")
                break
            except ValueError as ve:
                print(f"Error: {ve}. Please enter a valid number!")
        add_account = BankAccount.BankAccount(name, initial_balance)
        accounts.append(add_account)
        print("Added new person Successfully !")
    except Exception as e:
        print(f"Error adding account: {e}")



def select_account(accounts):
    '''
    it will select account chosen by the user
    '''
    try:
        if not accounts:
            raise ValueError("No accounts available.")
        selected_account = input("Please Enter account holder name to select : ").strip()
        if not selected_account:
            raise ValueError("Account holder name cannot be empty!")
        for acc in accounts:
            if acc.get_account_holder().lower() == selected_account.lower():
                return acc
        raise ValueError("Account not found. Please check the name and try again.")
    except Exception as e:
        print(f"Error selecting account: {e}")
        return None

accounts = []

print("Welcome to Bank Account System !")
while True:
    try:
        print(menu)
        choice = int(input("Please Enter Your Choice : "))
        if choice not in range(1, 7):
            raise ValueError("Invalid choice! Please enter a number between 1 and 7.")
        
        if choice == 1:
            add_new_account(accounts)
        elif choice == 2:
            selected_account = select_account(accounts)#to select account to deal with dopsit
            if selected_account is None:
                print("your selcet is wrong please Try again , select an exists account !")
                select_account(accounts) 
            else:
                try:
                    amount = float(input("Please Enter amount you want to deposit: ").strip())
                    if amount <= 0:
                        raise ValueError("Deposit amount must be greater than zero!")
                    selected_account.deposit(amount)
                    print("Deposit Successfully !")
                except ValueError as ve:
                    print(f"Error: {ve}")
                except Exception as e:
                    print(f"Error during deposit: {e}")
        elif choice == 3:
            selected_account = select_account(accounts)
            if selected_account is None:
                print("your selcet is wrong please Try again , select an exists account !")
                select_account(accounts)  
            else:
                try:
                    amount = float(input("Please Enter amount you want to withdraw: ").strip())
                    if amount <= 0:
                        raise ValueError("Withdrawal amount must be greater than zero!")
                    selected_account.withdraw(amount)
                    print("Withdraw Successfully !")
                except ValueError as ve:
                    print(f"Error: {ve}")
                except Exception as e:
                    print(f"Error during withdraw: {e}")
        elif choice == 4:
            selected_account = select_account(accounts)
            if selected_account is None:
                print("your selcet is wrong please Try again , select an exists account !")
                select_account(accounts)
            else:
                print(f"Account Holder Name : {selected_account.get_account_holder()}, Balance: {selected_account.get_balance()} $")
        elif choice == 6:
            print("Thank you for using the Bank Account System. Goodbye!")
            break
        elif choice == 5:
            if not accounts:
                print("No accounts available.")
            else:
                print("List of all accounts:")
                for i, acc in enumerate(accounts, 1):
                    print(f"{i}. Account Holder: {acc.get_account_holder()}, Balance: {acc.get_balance()} $")
    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")