class CustomerAccount:
    def __init__(self, fname, lname, address, account_no, balance):
        self.fname = fname
        self.lname = lname
        self.address = address
        self.account_no = account_no
        self.balance = float(balance)

    def update_first_name(self, fname):
        self.fname = fname
        print(self.fname)

    def update_last_name(self, lname):
        self.lname = lname
        print(self.lname)

    def get_first_name(self):
        return self.fname

    def get_last_name(self):
        return self.lname

    def update_address(self, addr):
        self.address = addr
        print(self.address)

    def get_address(self):
        return self.address

    def deposit(self, amount):
        self.balance += amount
        self.print_balance()

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            self.print_balance()
        else:
            print("Sorry, your credit is running low")

    def print_balance(self):
        print("\n The account balance is %.2f" % self.balance)

    def get_balance(self):
        return self.balance

    def get_account_no(self):
        return self.account_no

    def account_menu(self):
        print("\n Your Transaction Options Are:")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("1) Deposit money")
        print("2) Withdraw money")
        print("3) Check balance")
        print("4) Update customer name")
        print("5) Update customer address")
        print("6) Show customer details")
        print("7) Back")
        print(" ")
        option = int(input("Choose your option: "))
        return option

    def print_details(self):
        print(self.fname, self.lname, self.address, self.account_no, self.balance)

    def run_account_options(self):
        loop = 1
        while loop == 1:
            choice = self.account_menu()
            if choice == 1:
                amount = int(input('Deposit amount:'))
                self.deposit(amount)
            elif choice == 2:
                amount = int(input('Withdraw amount:'))
                self.withdraw(amount)
            elif choice == 3:
                self.print_balance()
            elif choice == 4:
                firstname = input("New firstname:")
                lastname = input("New lastname:")
                self.update_first_name(firstname)
                self.update_last_name(lastname)
            elif choice == 5:
                address = input("New address:")
                self.update_address(address)
            elif choice == 6:
                self.print_details()
            elif choice == 7:
                loop = 0
        print("\n Exit account operations")
