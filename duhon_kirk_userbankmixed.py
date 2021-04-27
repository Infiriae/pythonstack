class User:	
    counter = 0
    def __init__(self, name, email):
        User.counter+=1
        self.name = name
        self.email = email
        self.account = BankAccount()
        #Made "realistic" account ID
        #self.id = str(round(random.random()*8999+1000)+User.counter)
        self.id = User.counter
    def new_account(self):
        self.account = BankAccount()
        return self

    def make_deposit(self, amount):
        self.account.deposit(amount)
        print(self.name,'has deposited $'+str(amount),'into Account #'+str(self.id))
        return self

    def make_withdrawl(self, amount):
        if self.account.balance > amount:
            self.account.balance -= amount
            print(self.name,'has withdrawn $'+str(amount),'from Account #'+str(self.id))
        else:
            print(self.name+"'s account only has a $"+str(self.account.balance),'balance, cannot withdraw $'+str(amount))
        return self

    def display_user_balance(self):
        print(self.name,'currently has $'+str(self.account.balance),'in Account #'+str(self.id))
        return self

    def transfer_money(self, other, amount):
        if self.account.balance > amount:
            print(self.name,'has transferred $'+str(amount),'from Account #'+str(self.id),'to Account #'+str(other.id))
            self.account.balance -= amount
            other.account.balance += amount
        else:
            print(self.name+"'s Account #"+str(self.id),'does not have sufficient funds to transfer $'+str(amount))
        return self

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

john = User('Jonathan','BigJ@yahoo.com')
mal = User('Malory','Mal()ry@gmail.com')

mal.account.deposit(199).deposit(100).display_account_info()
john.new_account

print(john.__class__)
print(john.account.id)


print(john.account.balance)