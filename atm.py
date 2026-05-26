# ATM program

class ATM:
    def __init__(self):
        self.balance = 0

    def check_balance(self):
        """Users balance"""
        return self.balance
    
    def deposit(self, amount):
        """Allow users to deposit money to their account"""
        if amount <= 0:
            raise ValueError('\n❌ Error: Deposit amount must positive and greater than 0.')
        
        self.balance += amount

    def withdraw(self, amount):
        """Allow users to withdraw money from they account"""
        if amount <= 0:
            raise ValueError('\n❌ Error: Withdraw amount must be positive and greater than 0.')
        if amount > self.balance:
            raise ValueError('\nYou have insufficient funds in your account.')
        
        self.balance -= amount