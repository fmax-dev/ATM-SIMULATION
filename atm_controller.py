from atm import ATM

class ATMController():
    def __init__(self):
        self.atm = ATM()

    def get_number(self, user_input):
        """Taking users input for improved validation message"""
        while True:
            try:
                number = float(input(user_input))
                return number
            except ValueError:
                print("\n❌ Please enter a valid number")

    
    def displaying_menu(self):
        """Displaying the app's Menu"""
        print("\nATM MENU")
        print("  1. Check Balance")
        print("  2. Deposit")
        print("  3. Withdraw")
        print("  4. Exit")

    
    def display_balance(self):
        """Displaying balance to users"""
        balance = self.atm.check_balance()
        print(f"\nYour current balance is ${balance}")

    
    def making_deposits(self):
        """Allow users to make a deposit"""
        while True:
                try:
                    deposit_amount = self.get_number("\nEnter amount to deposit: ")
                        
                    self.atm.deposit(deposit_amount)
                    print(f"\n✅ You successfully deposited ${deposit_amount}.")
                    break
                except ValueError as error:
                    print(error)
    

    def making_withdraws(self):
        """Allow users to make a withdraw"""
        while True:
                try:
                    withdraw_amount = self.get_number("\nEnter amount to withdraw: ")
                        
                    self.atm.withdraw(withdraw_amount)
                    print(f"\n✅ You successfully withdrew ${withdraw_amount}.")
                    break
                except ValueError as error:
                    print(error)

    

    def run(self):
        """Responsible to run the UI Logic"""

        # GREETING
        print("\n----- WELCOME TO YOUR ATM MACHINE -----")

        while True:

            # DISPLAYING MENU
            self.displaying_menu()

            user_choice = input("\nPlease choose an option: ").strip()

            # ROUTING LOGIC
            if user_choice == "1":
                self.display_balance()
            #USER DEPOSITING MONEY
            elif user_choice == "2":
                self.making_deposits()
            # USERS WITHDRAWING MONEY
            elif user_choice == "3":
                self.making_withdraws()
            # USERS EXITING THE PROGRAM
            elif user_choice == "4":
                print("\nThank you for using the ATM!")
                break
            else:
                print("\nInvalid choice! Please try again.")


def main():
    controller = ATMController()
    controller.run()

if __name__ == "__main__":
    main()
