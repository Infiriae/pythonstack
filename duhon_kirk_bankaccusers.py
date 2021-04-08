userdb = []
class BankAccount:
    counter=0
    def __init__(self):
        BankAccount.counter+=1
        self.int_rate = 1.04
        self.balance = 0
        self.id = BankAccount.counter

    def deposit(self, amount):
        self.balance+=amount
        #people[f'{self}']
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

class User:	
    counter = 0
    def __init__(self, name, email):
        User.counter+=1
        userdb.append(self)
        self.name = name
        self.email = email
        self.accs = 1
        self.account = [BankAccount()]
        self.id = User.counter
        
        
    def make_deposit(self, amount):
        # self.account_balance += amount
        # print(self.name,'has deposited $'+str(amount),'into Account #'+str(self.id))
        return self

    def make_withdrawl(self, amount):
        # if self.account_balance > amount:
        #     self.account_balance -= amount
        #     print(self.name,'has withdrawn $'+str(amount),'from Account #'+str(self.id))
        # else:
        #     print(self.name+"'s account only has a $"+str(self.account_balance),'balance, cannot withdraw $'+str(amount))
        return self

    def display_user_balance(self):
        # print(self.name,'currently has $'+str(self.account_balance),'in Account #'+str(self.id))
        return self

    def transfer_money(self, other, amount):
        # if self.account_balance > amount:
        #     print(self.name,'has transferred $'+str(amount),'from Account #'+str(self.id),'to Account #'+str(other.id))
        #     self.account_balance -= amount
        #     other.account_balance += amount
        # else:
        #     print(self.name+"'s Account #"+str(self.id),'does not have sufficient funds to transfer $'+str(amount))
        return self
    
    def new_account(self):
        self.accs+=1
        self.account.append(BankAccount())
        return self

john = User('John','John@gmail.com')

maggie = User('Margaret','magpie@yahoo.com')

lee = User('Leon','leanmeanmachine@gmail.com')

for each in userdb:
    for every in each.account:
        every.deposit(500)

john.new_account().account[1].deposit(1)
john.new_account().account[2].deposit(3)
lee.new_account().account[1].deposit(4)
john.account[1].display_account_info()

for each in userdb:
    for every in each.account:
        every.deposit(500)

for x in userdb:
    if len(x.account) == 1:
        print(f'{x.name}\'s balance is ${x.account[0].balance}')
    else:
        for y in x.account:
            print(f'{x.name}\'s balance in Account #{y.id} is ${y.balance}')

# john.make_deposit(120).make_deposit(1000).make_withdrawl(655).display_user_balance()

# maggie.make_deposit(10000).make_deposit(3476).make_withdrawl(777).make_withdrawl(777).display_user_balance()


# lee.make_deposit(1500).make_withdrawl(1200).make_withdrawl(10).make_withdrawl(69).display_user_balance()


# john.transfer_money(lee, 175)
# lee.display_user_balance()
# john.display_user_balance()

exit()