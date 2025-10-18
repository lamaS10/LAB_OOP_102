class BankAccount:
    def __init__(self, account_holder: str, initial_balance: float = 0.0):
        try:
            if not account_holder or not isinstance(account_holder, str):
                raise ValueError("Account holder must be a non-empty string!")
            self._account_holder = account_holder
            self._balance = float(initial_balance)
            if self._balance < 0:
                raise ValueError("Initial balance cannot be negative!")
        except ValueError as ve:
            raise ValueError(f"Error initializing account: {ve}")

    def get_account_holder(self):
        '''
        it will get account holder because it's private attribute
        '''
        return self._account_holder
     
    def get_balance(self):
        '''
        it will get balnce because it's private attribute
        '''
        return self._balance

    def deposit(self, amount):
        '''
        it will calclute the deposit by balnce + amount
        '''
        amount = float(amount)
        self._balance += amount
        return self._balance


    def withdraw(self, amount):
        '''
        it will calclute the withdraw by balnce - amount
        '''
        try:
            amount = float(amount)
            if self._balance < amount:
                raise ValueError("Insufficient funds")
            self._balance -= amount
            return self._balance
        except ValueError as ve:
            raise ValueError(f"Withdraw error: {ve}")
