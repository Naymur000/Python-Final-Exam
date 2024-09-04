
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
        if bank.balance > amount:
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

