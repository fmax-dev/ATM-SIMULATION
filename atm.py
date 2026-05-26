# ATM program

class ATM:
    def __init__(self):
        self.balance = 0

    def check_balance(self):
        """Users balance"""
        return self.balance
    
    def deposit(self, amount):
        """Allow users to deposit money to their account"""
        if amount > 0:
            self.balance += amount
            return True
        elif amount == 0:
            return False
        else:
            return False

    def withdraw(self, amount):
        """Allow users to withdraw money from they account"""
        if amount > self.balance or amount <= 0:
            return False
        
        self.balance -= amount
        return True

def main():
    atm = ATM()

    print("\n----- WELCOME TO THE ATM MACHINE -----")

    # DISPLAYING MENU
    while True:
        print("\n--- ATM MENU ---")
        print("    1. Check Balance")
        print("    2. Deposit")
        print("    3. Withdraw")
        print("    4. Exit")

        user_choice = input("\nPlease choose an option: ").strip()

        # ROUTING LOGIC
        if user_choice == "1":
            balance = atm.check_balance()
            print(f"\nYour current balance is ${balance}")
        #USER DEPOSITING MONEY
        elif user_choice == "2":
            while True:
                try:
                    deposit_amount = float(input("\nEnter amount to deposit: "))
                    
                    if atm.deposit(deposit_amount):
                        print(f"\nYou successfully deposited ${deposit_amount}.")
                        break
                    elif deposit_amount == 0:
                        print(f"\nInvalid error: Amount must greater than 0.")
                    else:
                        print(f"\n${deposit_amount} must be positive.")
                except ValueError:
                    print("\nPlease enter a valid number")
        # USERS WITHDRAWING MONEY
        elif user_choice == "3":
            while True:
                try:
                    withdraw_amount = float(input("\nEnter amount to withdraw: "))
                    
                    if withdraw_amount <= 0:
                        print("\nWithdraw amount must be positive and greater than 0.")
                    elif not atm.withdraw(withdraw_amount):
                        print("\nYou have insufficient funds in your account.")
                    else:
                        print(f"\nYou successfully withdrew ${withdraw_amount}.")
                        break
                except ValueError:
                    print("\nPlease enter a valid number.")
        # USERS EXITING THE PROGRAM
        elif user_choice == "4":
            print("\nThank you for using the ATM!")
            break
        else:
            print("\nInvalid choice! Please try again.")

if __name__ == "__main__":
    main()