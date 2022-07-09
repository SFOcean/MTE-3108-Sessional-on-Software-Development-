
#Bank_Account class
class Bank_Account:
    def __init__(self):
        self.balance=0
        print("Deposit & Withdrawal Support Initiating.....")
 
    def depositMoney(self):
        amount=float(input("Enter amount to be Deposited: "))
        self.balance += amount
        print("\n Amount Deposited:",amount)
 
    def withdrawMoney(self):
        amount = float(input("Enter amount to be Withdrawn: "))
        if self.balance>=amount:
            self.balance-=amount
            print("\n You Withdrew:", amount)
        else:
            print("\n Insufficient balance  ")
 
    def showBalance(self):
        print("\n Net Available Balance=",self.balance)
 
# Driver code
  
# creating an object of class
s = Bank_Account()
  
# Calling functions with that class object
s.depositMoney()
s.withdrawMoney()
s.showBalance()