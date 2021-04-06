class BankAccount:
    counter=0
    def __init__(self):
        BankAccount.counter+=1
        self.int_rate = 1.04
        self.balance = 0
        self.id = BankAccount.counter

    def deposit(self, amount):
        self.balance+=amount
        return self

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance-=amount
            return self
        else:
            print(f'Account #{self.id} only contains ${self.balance}. Cannot withdraw ${amount}')
            return self

    def display_account_info(self):
        print('Account #'+str(self.id),'currently has $'+str(self.balance),'available.')
        return self

    def yield_interest(self):
        if self.balance > 0:
            self.balance = (self.balance * self.int_rate)
            return self

corp = BankAccount()
person = BankAccount()


corp.deposit(25000).deposit(7100).deposit(9650).withdraw(4000).yield_interest().display_account_info()

person.deposit(25000).deposit(7100).withdraw(200).withdraw(4000).withdraw(400).withdraw(1400).yield_interest().display_account_info()
