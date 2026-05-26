# ATM program

class ATM:
    def __init__(self):
        self.balance = 0

    def check_balance(self):
        """Users balance"""
        print(f"\nYour current balance is ${self.balance}")
    
    def deposit(self, amount):
        """Allow users to deposit money to their account"""
        if amount > 0:
            self.balance += amount
            print(f"\nSuccessfully deposited ${amount}.")
        elif amount == 0:
            print(f"\nInvalid error: Amount must greater than 0")
        else:
            print(f"\n${amount} must be positive")

    def withdraw(self, amount):
        """Allow users to withdraw money from they account"""
        if amount > self.balance:
            print("\nInsufficient amounts in your account")
        elif amount <= 0:
            print("\nWithdraw amount must positive or greater than 0")
        else:
            self.balance -= amount
            print(f"\n${amount} successfully withdrew")

def main():
    pass

if __name__ == "__main__":
    main()