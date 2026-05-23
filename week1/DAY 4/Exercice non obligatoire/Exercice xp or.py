class BankAccount:
    def __init__(self, username, password, balance=0):
        self.balance = balance
        self.username = username
        self.password = password
        self.authenticated = False

    def authenticate(self, username, password):
        if self.username == username and self.password == password:
            self.authenticated = True

    def deposit(self, amount):
        if not self.authenticated:
            raise Exception("You must be authenticated to deposit.")
        if amount <= 0:
            raise Exception("Deposit amount must be positive.")
        self.balance += amount

    def withdraw(self, amount):
        if not self.authenticated:
            raise Exception("You must be authenticated to withdraw.")
        if amount <= 0:
            raise Exception("Withdrawal amount must be positive.")
        self.balance -= amount


class MinimumBalanceAccount(BankAccount):
    def __init__(self, username, password, balance=0, minimum_balance=0):
        super().__init__(username, password, balance)
        self.minimum_balance = minimum_balance

    def withdraw(self, amount):
        if not self.authenticated:
            raise Exception("You must be authenticated to withdraw.")
        if amount <= 0:
            raise Exception("Withdrawal amount must be positive.")
        if self.balance - amount < self.minimum_balance:
            raise Exception(f"Cannot withdraw. Balance would go below minimum balance of {self.minimum_balance}.")
        self.balance -= amount


class ATM:
    def __init__(self, account_list, try_limit):
        for account in account_list:
            if not isinstance(account, (BankAccount, MinimumBalanceAccount)):
                raise Exception("account_list must contain BankAccount or MinimumBalanceAccount instances.")

        try:
            if try_limit <= 0:
                raise Exception("try_limit must be positive.")
        except Exception:
            try_limit = 2

        self.account_list = account_list
        self.try_limit = try_limit
        self.current_tries = 0
        self.show_main_menu()

    def show_main_menu(self):
        while True:
            print("\n--- ATM Main Menu ---")
            print("1. Login")
            print("2. Exit")
            choice = input("Select an option: ")
            if choice == "1":
                username = input("Enter username: ")
                password = input("Enter password: ")
                self.log_in(username, password)
            elif choice == "2":
                print("Goodbye!")
                break
            else:
                print("Invalid option.")

    def log_in(self, username, password):
        for account in self.account_list:
            account.authenticate(username, password)
            if account.authenticated:
                self.current_tries = 0
                self.show_account_menu(account)
                return

        self.current_tries += 1
        if self.current_tries >= self.try_limit:
            print("Maximum login attempts reached. Exiting.")
            exit()
        else:
            print(f"Invalid credentials. {self.try_limit - self.current_tries} attempt(s) remaining.")

    def show_account_menu(self, account):
        while True:
            print(f"\n--- Account Menu | Balance: {account.balance} ---")
            print("1. Deposit")
            print("2. Withdraw")
            print("3. Exit")
            choice = input("Select an option: ")
            if choice == "1":
                try:
                    amount = int(input("Enter deposit amount: "))
                    account.deposit(amount)
                    print(f"Deposited {amount}. New balance: {account.balance}")
                except Exception as e:
                    print(f"Error: {e}")
            elif choice == "2":
                try:
                    amount = int(input("Enter withdrawal amount: "))
                    account.withdraw(amount)
                    print(f"Withdrew {amount}. New balance: {account.balance}")
                except Exception as e:
                    print(f"Error: {e}")
            elif choice == "3":
                print("Logging out.")
                account.authenticated = False
                break
            else:
                print("Invalid option.")


acc1 = BankAccount("alice", "pass123", 500)
acc2 = MinimumBalanceAccount("bob", "secret", 300, minimum_balance=100)

ATM([acc1, acc2], 3)