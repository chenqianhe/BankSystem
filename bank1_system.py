from customer_account import CustomerAccount
from admin import Admin

accounts_list = []
admins_list = []


class BankSystem(object):
    def __init__(self):
        self.accounts_list = []
        self.admins_list = []
        self.load_bank_data()

    def load_bank_data(self):

        # create customers
        account_no = 1234
        customer_1 = CustomerAccount("Adam", "Smith", ["14", "Wilcot Street", "Bath", "B5 5RT"], account_no, 5000.00)
        self.accounts_list.append(customer_1)

        account_no += 1
        customer_2 = CustomerAccount("David", "White", ["60", "Holborn Viaduct", "London", "EC1A 2FD"], account_no,
                                     3200.00)
        self.accounts_list.append(customer_2)

        account_no += 1
        customer_3 = CustomerAccount("Alice", "Churchil", ["5", "Cardigan Street", "Birmingham", "B4 7BD"], account_no,
                                     18000.00)
        self.accounts_list.append(customer_3)

        account_no += 1
        customer_4 = CustomerAccount("Ali", "Abdallah", ["44", "Churchill Way West", "Basingstoke", "RG21 6YR"],
                                     account_no, 40.00)
        self.accounts_list.append(customer_4)

        # create admins
        admin_1 = Admin("Julian", "Padget", ["12", "London Road", "Birmingham", "B95 7TT"], "id1188", "1441", True)
        self.admins_list.append(admin_1)

        admin_2 = Admin("Cathy", "Newman", ["47", "Mars Street", "Newcastle", "NE12 6TZ"], "id3313", "2442", False)
        self.admins_list.append(admin_2)

    def search_admins_by_name(self, admin_username):
        for admins in self.admins_list:  # STEP A.3
            if admin_username == admins.user_name:
                return admins
            else:
                print("The account does not exist!")
                return None

    def search_customers_by_name(self, customer_lname):
        for customers in self.accounts_list:  # STEP A.3
            if customer_lname == customers.lname:
                return customers
            else:
                print("The account does not exist!")
                return None

    def main_menu(self):
        # print the options you have
        print()
        print()
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("Welcome to the Python Bank System")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("1) Admin login")
        print("2) Quit Python Bank System")
        print(" ")
        option = int(input("Choose your option: "))
        return option

    def run_main_options(self):
        loop = 1
        while loop == 1:
            choice = self.main_menu()
            if choice == 1:
                username = input("\n Please input admin username: ")
                password = input("\n Please input admin password: ")
                msg, admin_obj = self.admin_login(username, password)
                print(msg)
                if admin_obj is not None:
                    self.run_admin_options(admin_obj)
            elif choice == 2:
                loop = 0
        print("\n Thank-You for stopping by the bank!")

    def transferMoney(self, sender_lname, receiver_lname, receiver_account_no, amount):
        for user in self.accounts_list:  # Judge whether the transferor exists
            if sender_lname == user.lname:
                for user2 in self.accounts_list:  # Judge whether the receiving account exists
                    if receiver_lname == user2.lname:  # Judge whether the receiving account number corresponds to the receiver
                        if int(receiver_account_no) == user2.account_no:
                            if amount <= user.balance:  # Judge whether the transfer amount is legal
                                user.balance = user.balance - amount
                                user2.blance = user2.balance + amount
                                print("Transfer succeeded!Your current balance is %f" % user.balance)
                                return
                            else:
                                print("Insufficient account balance！")
                                return
                        else:
                            print("Wrong receiving account number！")
                            return
                print("Recipient does not exist！")
                return
        print("Transferor does not exist!")
        return

    def admin_login(self, username, password):
        for admin in self.admins_list:  ####### 1
            if username == admin.user_name:
                if password == admin.password:
                    return "Login successful！", admin
                else:
                    return "Password error！", None
        return "Account does not exist!", None

    def admin_menu(self, admin_obj):
        # print the options you have
        print(" ")
        print("Welcome Admin %s %s : Avilable options are:" % (admin_obj.get_first_name(), admin_obj.get_last_name()))
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("1) Transfer money")
        print("2) Customer account operations & profile settings")
        print("3) Delete customer")
        print("4) Print all customers detail")
        print("5) Sign out")
        print(" ")
        option = int(input("Choose your option: "))
        return option

    def run_admin_options(self, admin_obj):
        loop = 1
        while loop == 1:
            choice = self.admin_menu(admin_obj)
            if choice == 1:
                sender_lname = input("\n Please input sender username: ")
                amount = float(input("\n Please input the amount to be transferred: "))
                receiver_lname = input("\n Please input receiver surname: ")
                receiver_account_no = input("\n Please input receiver account number: ")
                self.transferMoney(sender_lname, receiver_lname, receiver_account_no, amount)

            elif choice == 2:
                customer_lname = input("\n Please input customer lastname:  ")
                customer = self.search_customers_by_name(customer_lname)
                customer.run_account_options()

            elif choice == 3:
                customer_lname = input("\n Please input customer lastname:  ")  # STEP A.5
                customer = self.search_customers_by_name(customer_lname)
                if customer is not None:
                    Delete_customernumber = int(input("\n Please input cunstomer account number: "))
                    if Delete_customernumber == customer.account_no:
                        self.accounts_list.remove(customer)
                    else:
                        print("Wrong receiving account number！")

            elif choice == 4:
                self.print_all_accounts_details()

            elif choice == 5:
                loop = 0
        print("\n Exit account operations")

    def print_all_accounts_details(self):
        # list related operation - move to main.py
        i = 0
        for c in self.accounts_list:
            i += 1
            print('\n %d. ' % i, end=' ')
            c.print_details()
            print("------------------------")


app = BankSystem()
app.run_main_options()
