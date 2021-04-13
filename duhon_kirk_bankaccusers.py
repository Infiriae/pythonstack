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
        
        
    def make_deposit(self, acc, amount):
        if acc <= self.accs:
            self.account[acc-1].deposit(amount)
        else:
            print("Account not recognized. please choose account (account, amount)")
        return self

    def make_withdrawl(self, acc, amount):
        # if self.account_balance > amount:
        #     self.account_balance -= amount
        #     print(self.name,'has withdrawn $'+str(amount),'from Account #'+str(self.id))
        # else:
        #     print(self.name+"'s account only has a $"+str(self.account_balance),'balance, cannot withdraw $'+str(amount))
        return self

    def display_user_balance(self, acc):
        if acc <= self.accs:
            print(f'{self.name}\'s'), self.account[acc-1].display_account_info()
        else:
            print("Account not recognized. please choose account (account, amount)")
        return self

    def transfer_money(self, acc, tar, tacc, amount):
        if acc <= self.accs and tacc <= tar.accs:
            if self.account[acc-1].balance > amount:
                print(self.name,'has transferred $'+str(amount),'from Account #'+str(self.id),'to Account #'+str(tar.id))
                self.account[acc-1].balance -= amount
                tar.account[tacc-1].balance += amount
            else:
                print(self.name+"'s Account #"+str(self.id),'does not have sufficient funds to transfer $'+str(amount))
        else:
            print("Account not recognized. please choose account (your account, who to give, their account, amount)")
        return self
    
    def new_account(self):
        self.accs+=1
        self.account.append(BankAccount())
        return self

john = User('John','John@gmail.com')

maggie = User('Margaret','magpie@yahoo.com')

lee = User('Leon','leanmeanmachine@gmail.com')

for each in userdb:
    for x in range(len(each.account)):
        each.make_deposit(x,500)    

john.new_account().make_deposit(2,100)
john.new_account().make_deposit(3,10)
lee.new_account().make_deposit(2,4)
john.transfer_money(1,lee,1,100).make_deposit(1,200)

for z in range(john.accs):
    john.display_user_balance(z)

for each in userdb:
    for x in range(len(each.account)):
        each.make_deposit(x,500)

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