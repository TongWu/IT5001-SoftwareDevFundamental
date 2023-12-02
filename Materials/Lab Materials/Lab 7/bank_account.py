
class BankAccount():
    def __init__(self,name,balance):
        self.name = name
        self.balance = balance
    def withdraw(self,amount):
        if self.balance < amount:
            print(f"Money not enough! You do not have ${amount:.2f}")
            return 0
        else:
            self.balance -= amount
            return amount
    def showBalance(self):
        print(f'Your balance is ${self.balance:.2f}')

myAcc = BankAccount('Alan',1000)
johnAcc = BankAccount('John Wick',100000000)
              
myAcc.showBalance()
myAcc.withdraw(123)
myAcc.showBalance()
myAcc.withdraw(99999)



        
    
