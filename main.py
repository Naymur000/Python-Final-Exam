
class Account:

    def __init__(self, name, email , address, acc_type, password):
        self.name = name
        self.email = email
        self.address = address
        self.acc_type = acc_type
        self.password = password
        self.balance = 0
        self.loan_times = 0
        self.transaction = []
        self.loan_balance = 0


    def deposit(self, amount):
        self.balance += amount
        self.transaction.append(f"{amount} Taka is deposited")
        print("Deposit is successful")


    def withdraw(self, bank, amount):
        if bank.get_available_balance() > amount:
            if self.balance >= amount:
                self.balance -= amount
                self.transaction.append(f"{amount} Taka is withdrawn")
                print(f"{amount} Taka is withdrawn successfully")
            else:
                print("Withdrawal amount exceeded")
        else:
            print("The Bank is bankrupt")


    def check_balance(self):
        print(f"Your account balance is {self.balance}")


    def check_loan(self):
        print(f"Your loan balance is {self.loan_balance}")


    def transaction_history(self):
        count = 1
        print("*-- Your Transaction history --*")
        for tran in self.transaction:
            print(f'{count}. {tran}')
            count += 1


    def take_loan(self, bank, amount):
        if bank.loan_feature:
            if self.loan_times < 2:
                if bank.get_available_balance() > amount:
                    self.balance += amount
                    self.loan_balance += amount
                    self.transaction.append(f"{amount} Taka taken as loan")
                    self.loan_times += 1
                    print(f"{amount} Taka Loan is issued")
                else:
                    print("Not enough money")
            else:
                print("Loantimes exceeded!!")
        else:
            print("Loan is not issued")


    def return_loan(self, amount):
        if self.balance >= amount:
            if self.loan_balance > 0 and amount <= self.loan_balance:
                self.balance -= amount
                self.loan_balance -= amount
                self.loan_times += 1
                if self.loan_times > 2:
                    self.loan_times = 2
                print(f"{amount} Taka loan is returned successfully")
                self.transaction.append(f"{amount} Taka loan is returned")
            elif self.loan_balance > 0 and amount > self.loan_balance:
                self.balance -= self.loan_balance
                self.loan_times += 1
                if self.loan_times > 2:
                    self.loan_times = 2
                self.loan_balance = 0
                print(f"Total loan is returned successfully")
                self.transaction.append(f"{self.loan_balance} Taka loan is returned")
            elif self.loan_balance <= 0:
                print("You don't have any loan")
        else:
            print("Insufficient balance to return loan !!")


    def transfer(self, receiver_number, sender_number, amount, bank):
        if receiver_number in bank.users:
            receiver = bank.users[receiver_number]
            if self.balance >= amount:
                self.balance -= amount
                receiver.balance += amount
                self.transaction.append(f"{amount} Taka transeferred to account number: {receiver_number}")
                receiver.transaction.append(f"{amount} Taka received from account number: {sender_number}")
                print("Transaction successful")
            else:
                print("Insufficient balance !!")
        else:
            print("Invalid account number !!")



class Bank:

    def __init__(self, name):
        self.name = name
        self.balance = 0
        self.users = {}
        self.total_loan = 0
        self.available_balance = 0
        self.loan_feature = True
        self.count = 1000000

    def create_account(self, name, email , address, acc_type, password):
        account = Account(name, email , address, acc_type, password)
        account_number = self.count
        self.count += 1
        self.users[account_number] = account
        print(f"Account created successfully.\n Your account number is: {account_number}")

    def delete_account(self, account_number):
        if account_number in self.users:
            del self.users[account_number]
            print("Account is deleted successfully")
        else:
            print("Account doesn't exist")

    def get_all_accounts(self):
        print(f"Name\tAccount_type\tAccount_number")
        for key, value in self.users.items():
            print(f"{value.name}\t{value.acc_type}\t\t{key}")

    def get_total_loan(self):
        self.total_loan = 0
        for value in self.users.values():
            self.total_loan += value.loan_balance
        return self.total_loan

    def get_total_balance(self):
        self.balance = 0 
        for value in self.users.values():
            self.balance += value.balance
        return self.balance

    def get_available_balance(self):
        self.available_balance = 0
        self.available_balance = self.get_total_balance() - self.get_total_loan()
        return self.available_balance

    def set_loan_feature(self, status):
        self.loan_feature = status
        if status:
            print("Loan feature is enabled")
        else:
            print("Loan feature is disabled")



def registration():
    name = input("Enter your name: ")
    email = input("Enter your email: ")
    password = input("Enter your password: ")
    address = input("Enter your address: ")
    account_type = "Other"
    print("Choose your account type")
    print("""
    1. Savings
    2. Current
              """)
    option = int(input("Enter an option: "))
    if option == 1:
        account_type = "Savings"
    elif option == 2:
        account_type = "Current"

    bank.create_account(name, email , address, account_type, password)


def USER_LOGIN():
    user = user_login()
    if user:
        while True:
            print("""
        ---------------
        |  User Menu  |
        ---------------
                      """)
            print()
            print("1. Execute Trasaction(Deposit or Withdraw)")
            print("2. Check Balance")
            print("3. Transfer Balance to Another Account")
            print("4. Take Loan")
            print("5. Transaction History")
            print("6. Return Loan")
            print("7. Check Loan Amount")
            print("8. Logout")
            print()

            choose = int(input("Enter your option: "))
            if choose == 1:
                print("**-- Choose Deposit/Withdrawal --**")
                transactoin = input("Enter transaction: ")
                if transactoin == "Deposit":
                    amount = int(input("Enter deposit amount:"))
                    user.deposit(amount)
                elif transactoin == "Withdraw":
                    amount = int(input("Enter withdrawal amount: "))
                    user.withdraw(bank, amount)
            elif choose == 2:
                user.check_balance()
            elif choose == 3:
                receiver_number = int(input("Enter receiver acc_number: "))
                sender_number = int(input("Enter sender acc_number: "))
                amount = int(input("Enter amount: "))    
                user.transfer(receiver_number, sender_number, amount, bank)
            elif choose == 4:
                amount = int(input("Enter amount: "))
                user.take_loan(bank, amount)
            elif choose == 5:
                user.transaction_history()
            elif choose == 6:
                amount = int(input("Enter amount: "))
                user.return_loan(amount)
            elif choose == 7:
                user.check_loan()
            elif choose == 8:
                break
            else:
                print("Invalid option !!")



def ADMIN_LOGIN():
    admin = admin_login()
    if admin:
        while True:
            print()
            print("""
        -----------------
        |  Admin Menu   |
        -----------------
                    """)
            print()
            print("1. Create Account")
            print("2. Delete Account")
            print("3. See All User List")
            print("4. See Total Balance of Bank")
            print("5. See Total Loan")
            print("6. Toggle loan Feature")
            print("7. Logout")
            print()

            choose = int(input("Enter your option: "))
            if choose == 1:
                registration()
                
            elif choose == 2:
                account_number = int(input("Enter acc_number to be deleted: "))
                bank.delete_account(account_number)
                
            elif choose == 3:
                print("All accounts: ")
                bank.get_all_accounts()
                
            elif choose == 4:
                print("Total balance of the bank: ",bank.get_available_balance())
                
            elif choose == 5:
                print("Total Loan of the bank: ",bank.get_total_loan())
                
            elif choose == 6:
                print("Choice Status ")
                print("1. True ")
                print("2. False ")
                status = True
                c = input("Enter type: ")
                if c == "1":
                    status = True
                elif c == "2":
                    status = False
                bank.set_loan_feature(status)
                
            elif choose == 7:
                break
            else:
                print("Invalid option !!")



def user_login():
    acc_number = int(input("Enter your account number: "))
    acc_password = input("Enter your password: ")
    if acc_number in bank.users:
        if acc_password in bank.users[acc_number].password:
            return bank.users[acc_number]
        else:
            print("wrong password")
            return None
    else:
        print("Invalid account number !!")
        return None


def admin_login():
    username = input("Enter username: ")
    password = input("Enter password: ")
    if username == "admin" and password == "admin":
        return True
    else:
        print("Invalid admin username & password")
        return False


bank = Bank("XM Bank")

while True:
    print("""
          -----------------------------------------
          | Welcome to the bank management system |
          -----------------------------------------
            """)
    print()
    print("1. Registration & Create Account")
    print("2. User Login")
    print("3. Admin Login")
    print("4. Exit")
    print()
    
    choose = int(input("Enter your option: "))
    if choose == 1:
        registration()
    elif choose == 2:
        USER_LOGIN()
    elif choose == 3:
        ADMIN_LOGIN()
    elif choose == 4:
        break
    else:
        print("Invalid option !!")