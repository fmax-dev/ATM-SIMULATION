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

def main():
    atm = ATM()

    print("\n----- WELCOME TO YOUR ATM MACHINE -----")

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
                    
                    atm.deposit(deposit_amount)
                    print(f"\n✅ You successfully deposited ${deposit_amount}.")
                    break
                except ValueError as error:
                    print(error)
        # USERS WITHDRAWING MONEY
        elif user_choice == "3":
            while True:
                try:
                    withdraw_amount = float(input("\nEnter amount to withdraw: "))
                    
                    atm.withdraw(withdraw_amount)
                    print(f"\n✅ You successfully withdrew ${withdraw_amount}.")
                    break
                except ValueError as error:
                    print(error)
        # USERS EXITING THE PROGRAM
        elif user_choice == "4":
            print("\nThank you for using the ATM!")
            break
        else:
            print("\nInvalid choice! Please try again.")

if __name__ == "__main__":
    main()