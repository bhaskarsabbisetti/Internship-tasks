class ATM:
    def __init__(self, balance=0, pin="1234"):
        self.balance = balance
        self.pin = pin

    def verify_pin(self):
        attempts = 3
        while attempts > 0:
            entered_pin = input("Enter your PIN: ")
            if entered_pin == self.pin:
                print("PIN verified successfully!\n")
                return True
            else:
                attempts -= 1
                print(f"Incorrect PIN. {attempts} attempt(s) remaining.")
        print("Too many incorrect attempts. Exiting.")
        return False

    def check_balance(self):
        print(f"Your current balance is ₹{self.balance}\n")

    def deposit(self):
        try:
            amount = float(input("Enter amount to deposit: ₹"))
            if amount <= 0:
                print("Please enter a valid amount.\n")
                return
            self.balance += amount
            print(f"₹{amount} deposited successfully.\n")
        except ValueError:
            print("Invalid input. Please enter a number.\n")

    def withdraw(self):
        try:
            amount = float(input("Enter amount to withdraw: ₹"))
            if amount <= 0:
                print("Please enter a valid amount.\n")
            elif amount > self.balance:
                print("Insufficient balance.\n")
            else:
                self.balance -= amount
                print(f"₹{amount} withdrawn successfully.\n")
        except ValueError:
            print("Invalid input. Please enter a number.\n")

    def change_pin(self):
        old_pin = input("Enter current PIN: ")
        if old_pin != self.pin:
            print("Incorrect current PIN.\n")
            return
        new_pin = input("Enter new 4-digit PIN: ")
        if len(new_pin) == 4 and new_pin.isdigit():
            self.pin = new_pin
            print("PIN changed successfully.\n")
        else:
            print("Invalid PIN format. Must be 4 digits.\n")

    def menu(self):
        if not self.verify_pin():
            return
        while True:
            print("\n=== ATM Menu ===")
            print("1. Check Balance")
            print("2. Deposit Money")
            print("3. Withdraw Money")
            print("4. Change PIN")
            print("5. Exit")
            choice = input("Choose an option: ")

            if choice == '1':
                self.check_balance()
            elif choice == '2':
                self.deposit()
            elif choice == '3':
                self.withdraw()
            elif choice == '4':
                self.change_pin()
            elif choice == '5':
                print("Thank you for using our ATM. Have A Great Day")
                break
            else:
                print("Invalid option. Please try again.\n")
atm = ATM(balance=5000)
atm.menu()