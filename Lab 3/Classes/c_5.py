class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, num):
        self.balance += num
        print(f"Current balance: {self.balance}")

    def withdrawal(self, num):
        if self.balance - num >= 0:
            self.balance -= num 
        else:
            print("There are not enough funds to withdraw from the account:")
        
        print(f"Current balance: {self.balance}")

p = Account("Sultan", 0)

p.deposit(100)
p.withdrawal(100)
p.withdrawal(200)