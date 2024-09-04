from account import Account

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

