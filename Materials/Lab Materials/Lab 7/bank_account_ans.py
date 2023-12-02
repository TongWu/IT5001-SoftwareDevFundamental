
class BankAccount():
    def __init__(self, name, balance, interestrate):
        self.name = name
        self.balance = balance
        self.ir = interestrate
        self.giro = 0
    def withdraw(self, name, amount):
        if name != self.name:
            print("You are not authorized for this account")
            return
        if self.balance < amount:
            print(f"Money not enough! You do not have ${amount:.2f}")
            return 0
        else:
            self.balance -= amount
            return amount
    def deposit(self, amount):
        self.balance += amount
    def oneYearHasPassed(self):
        self.withdraw(self.name, self.giro)
        self.balance *= 1 + self.ir
    def transferTo(self, name, account, amount):
        if self.withdraw(name, amount):
            account.deposit(amount)
    def setupGiro(self, amount):
        self.giro += amount
    def showBalance(self):
        print(f'Your balance is ${self.balance:.2f}')

class MinimalAccount(BankAccount):
    def oneYearHasPassed(self):
        if self.balance < 1000:
            self.balance = max(self.balance - 20,0)
        super().oneYearHasPassed()

class JointAccount(BankAccount):
    def __init__(self, name, name2, balance, interestrate):
        super().__init__(name, balance, interestrate)
        self.name2 = name2
    def withdraw(self, name, amount):
        if name != self.name and name != self.name2:
            print("You are not authorized for this account")
            return
        if self.balance < amount:
            print(f"Money not enough! You do not have ${amount:.2f}")
            return 0
        else:
            self.balance -= amount
            return amount
