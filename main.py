from Bank import Bank

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