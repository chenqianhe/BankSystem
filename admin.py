

class Admin:
    
    def __init__(self, fname, lname, address, user_name, password, full_rights):
        self.fname = fname
        self.lname = lname
        self.address = address
        self.user_name = user_name
        self.password = password
        self.full_admin_rights = full_rights
    
    def update_first_name(self, fname):
        self.fname = fname
    
    def update_last_name(self, lname):
        self.lname = lname
                
    def get_first_name(self):
        return self.fname
    
    def get_last_name(self):
        return self.lname
        
    def update_address(self, addr):
        self.address = addr
    
    def set_username(self, uname):
        self.user_name = uname
        
    def get_username(self):
        return self.user_name
        
    def get_address(self):
        return self.address      
    
    def update_password(self, password):
        self.password = password
    
    def get_password(self):
        return self.password
    
    def set_full_admin_right(self, admin_right):
        self.full_admin_rights = admin_right

    def has_full_admin_right(self):
        return self.full_admin_rights

    def admin_menu(self):
        print("\n Your Transaction Options Are:")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("1) Update your name")
        print("2) Update your address")
        print("3) Back")
        print(" ")
        option = int(input("Choose your option: "))
        return option

    def run_admin_options2(self):
        loop = 1
        while loop == 1:
            choice = self.admin_menu()

            if choice == 1:
                firstname = input("Please enter a new firstname:")
                lastname = input("Please enter a new lasttname:")
                self.update_first_name(firstname)
                self.update_last_name(lastname)

            elif choice == 2:
                address = {'n': input("\n Please input your Number:  "),
                           'street': input("\n Please input your street:  "),
                           'town': input("\n Please input your town:  "),
                           'PostCode': input("\n Please input your PostCode:  ")}
                self.update_address(address)

            elif choice == 3:
                loop = 0
        print("\n Exit account operations")



