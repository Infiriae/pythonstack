#import random

class User:	
    counter = 0
    def __init__(self, name, email):
        User.counter+=1
        self.name = name
        self.email = email
        self.account_balance = 0
        #Made "realistic" account ID
        #self.id = str(round(random.random()*8999+1000)+User.counter)
        self.id = User.counter
        
    def make_deposit(self, amount):
        self.account_balance += amount
        print(self.name,'has deposited $'+str(amount),'into Account #'+str(self.id))
        return self

    def make_withdrawl(self, amount):
        if self.account_balance > amount:
            self.account_balance -= amount
            print(self.name,'has withdrawn $'+str(amount),'from Account #'+str(self.id))
        else:
            print(self.name+"'s account only has a $"+str(self.account_balance),'balance, cannot withdraw $'+str(amount))
        return self

    def display_user_balance(self):
        print(self.name,'currently has $'+str(self.account_balance),'in Account #'+str(self.id))
        return self

    def transfer_money(self, other, amount):
        if self.account_balance > amount:
            print(self.name,'has transferred $'+str(amount),'from Account #'+str(self.id),'to Account #'+str(other.id))
            self.account_balance -= amount
            other.account_balance += amount
        else:
            print(self.name+"'s Account #"+str(self.id),'does not have sufficient funds to transfer $'+str(amount))
        return self

john = User('John','John@gmail.com')
maggie = User('Margaret','magpie@yahoo.com')
lee = User('Leon','leanmeanmachine@gmail.com')

john.make_deposit(120).make_deposit(1000).make_withdrawl(655).display_user_balance()
# john.make_deposit(1000)
# john.make_withdrawl(60003)
# john.display_user_balance()

maggie.make_deposit(10000).make_deposit(3476).make_withdrawl(777).make_withdrawl(777).display_user_balance()
# maggie.make_deposit(3476)
# maggie.make_withdrawl(777)
# maggie.make_withdrawl(777)
# maggie.display_user_balance()

lee.make_deposit(1500).make_withdrawl(1200).make_withdrawl(10).make_withdrawl(69).display_user_balance()
# lee.make_withdrawl(1200)
# lee.make_withdrawl(10)
# lee.make_withdrawl(69)
# lee.display_user_balance()

john.transfer_money(lee, 175)
lee.display_user_balance()
john.display_user_balance()