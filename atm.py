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
            print(f"\nYou successfully deposited ${amount}.")
        elif amount == 0:
            print(f"\nInvalid error: Amount must greater than 0.")
        else:
            print(f"\n${amount} must be positive.")

    def withdraw(self, amount):
        """Allow users to withdraw money from they account"""
        if amount > self.balance:
            print("\nYou have insufficient funds in your account.")
        elif amount <= 0:
            print("\nWithdraw amount must positive or greater than 0.")
        else:
            self.balance -= amount
            print(f"\nYou successfully withdrew ${amount}.")

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
            atm.check_balance()
        elif user_choice == "2":
            while True:
                try:
                    deposit_amount = float(input("\nEnter amount to deposit: "))
                    atm.deposit(deposit_amount)
                    break
                except ValueError:
                    print("\nPlease enter a valid number")
        elif user_choice == "3":
            while True:
                try:
                    withdraw_amount = float(input("\nEnter amount to withdraw: "))
                    atm.withdraw(withdraw_amount)
                    break
                except:
                    print("\nPlease enter a valid number.")
        elif user_choice == "4":
            print("\nThank you for using the ATM!")
            break
        else:
            print("\nInvalid choice! Please try again.")

if __name__ == "__main__":
    main()