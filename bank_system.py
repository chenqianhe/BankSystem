from customer_account1 import CustomerAccount
from admin import Admin
import json

accounts_list = []
admins_list = []


class BankSystem(object):
    def __init__(self):
        self.accounts_list = []
        self.admins_list = []
        self.load_bank_data()

    def load_bank_data(self):

        with open('data.json') as f:
            data = json.load(f)

        for c in data["Customer"]:
            accounts_list.append(CustomerAccount(c["fName"], c["sName"], c["address"], c["cid"], c["balance"],
                                                 c["category"], c["interest"], c["loan"]))

        for a in data["Admin"]:
            admins_list.append(Admin(a["fName"], a["sName"], a["address"], a["aid"], a["password"],
                                     a["adminRight"]))

    def search_admins_by_name(self, admin_username):
        # STEP A.2
        l = []  # handles more than one admin with thwe same surname
        for a in admins_list:
            if a.lname == admin_username:
                l.append(a)
        return l

    def search_customers_by_name(self, customer_lname):
        # STEP A.3
        l = []  # handles more than one customer with the same surname
        for a in accounts_list:
            if a.lname == customer_lname:
                l.append(a)
        return l

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
                print('-' * 30, '\n', msg, '\n', '-' * 30)
                if admin_obj != None:
                    self.run_admin_options(admin_obj)
            elif choice == 2:
                loop = 0
        print("\n Thank-You for stopping by the bank!")

    def transferMoney(self, sender_ID, receiver_ID, amount):
        ## check if sender and reciver exist
        for count1 in accounts_list:
            if sender_ID == int(count1.account_no):
                for count2 in accounts_list:
                    if receiver_ID == int(count2.account_no):
                        if count1.balance >= amount:
                            count1.balance -= amount
                            count2.balance += amount
                            print("Transfer succeeded!Your current balance is %f" % count1.balance)
                            return
                        else:
                            print("Wrong receiving account number！")
                            return
        print("Transferor or Recipient does not exist！")
        

    def admin_login(self, username, password):
        # STEP A.1
        for admin in admins_list:  ####### 1
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
        print("3) Administrator account operations and profile settings")
        print("4) Delete customer")
        print("5) Print all customers detail")
        print("6) Create a new type of bank account")
        print(
            "7) Application management report")  # Total number of customers in the system， The sum of all the money，Total interest rate payable in one year， Total amount of overdraft
        print("8) Sign out")
        print(" ")
        option = int(input("Choose your option: "))
        return option

    def run_admin_options(self, admin_obj):
        loop = 1
        while loop == 1:
            choice = self.admin_menu(admin_obj)
            if choice == 1:
                sender_ID = int(input("\n Please input sender ID: "))
                amount = float(input("\n Please input the amount to be transferred: "))
                receiver_ID = int(input("\n Please input receiver ID: "))
                self.transferMoney(sender_ID, receiver_ID, amount)
            elif choice == 2:
                customer_lname = input("\n Please input customer lastname:  ")
                customers = self.search_customers_by_name(customer_lname)
                if not customers:
                    print("Account does not exist")
                else:
                    for customer in customers:
                        print(customer.fname, customer.lname, customer.account_no, customer.category)
                        customer.run_account_options()
            elif choice == 3:
                admin_obj.run_admin_options2()
            elif choice == 4:
                customer_lname = input("\n Please input customer lastname:  ")  # STEP A.5
                customers = self.search_customers_by_name(customer_lname)
                if not customers:
                    print("Account does not exist")
                else:
                    customer_ID = int(input("\n Please input customer ID:"))
                    for customer in customers:
                        if customer_ID == customer.account_no:
                            accounts_list.remove(customer)
            elif choice == 5:
                self.print_all_accounts_details()
            elif choice == 6:
                self.create_a_new_account()
            elif choice == 7:
                self.print_management_report()
            elif choice == 8:
                self.store_file()
                loop = 0
        print("\n Exit account operations")

    def create_a_new_account(self):
        address = {}
        category = int(input("\n Please input category:  "))
        fname = input("\n Please input customer firstname:  ")
        lname = input("\n Please input customer lastname:  ")
        address['n'] = int(input("\n Please input customer Number:  "))
        address['street'] = input("\n Please input customer street:  ")
        address['town'] = input("\n Please input customer town:  ")
        address['PostCode'] = input("\n Please input customer PostCode:  ")
        account_no = accounts_list[-1].account_no + 1
        balance = float(input("\n Please input customer balance:  "))

        if category == 1:
            accounts_list.append(CustomerAccount(fname, lname, address, account_no, balance, category, 0.3, 3000))
        elif category == 2:
            accounts_list.append(CustomerAccount(fname, lname, address, account_no, balance, category, 0.5, 5000))
        elif category == 3:
            accounts_list.append(CustomerAccount(fname, lname, address, account_no, balance, category, 0.2, 1000))

    def print_all_accounts_details(self):
        # list related operation - move to main.py
        i = 0
        for c in accounts_list:
            i += 1
            print('\n %d. ' % i, end=' ')
            c.print_details()
            print("------------------------")

    def print_management_report(self):
        customer_count = 0
        customer = []
        infom = []
        for c in accounts_list:
            if [c.fname, c.lname, c.address] not in customer:
                customer_count += 1
                customer.append([c.fname, c.lname, c.address])

        print("Sum of customer: ", customer_count)

        for i in range(customer_count):
            infom.append([0., 0., 0.])  # balance, interest, loan
            for c in accounts_list:
                if [c.fname, c.lname, c.address] == customer[i]:
                    infom[i][0] += c.balance
                    infom[i][1] += c.balance * c.interest
                    infom[i][2] += c.loan
            print('\n %d. ' % (i + 1))
            for data in customer[i]:
                print(data)
            print('balance', infom[i][0])
            print('interest', infom[i][1])
            print('loan', infom[i][2])

    def store_file(self):
        all = {"Customer": [], "Admin": []}
        for c in accounts_list:
            all["Customer"].append({"cid": c.account_no, "fName": c.fname, "sName": c.lname, "balance": c.balance,
                                    "category": c.category, "interest": c.interest, "loan": c.loan, "address": c.address
                                    })
        for a in admins_list:
            all["Admin"].append({"aid": a.user_name, "fName": a.fname, "sName": a.lname, "password": a.password,
                                 "adminRight": a.full_admin_rights, "address": a.address})

        with open('data.json', 'w') as f:
            json.dump(all, f)


app = BankSystem()
app.run_main_options()
