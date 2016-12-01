#Main class
class Account(object):
    def __init__(self, holder, number, balance,credit_line=2000): 
        self.Holder = holder 
        self.Number = number 
        self.Balance = balance
        self.CreditLine = credit_line
    #Deposit method
    def deposit(self, amount): 
        self.Balance = amount
    #Withdraw method
    def withdraw(self, amount): 
        if(self.Balance - amount < -self.CreditLine):
            return False  
        else: 
            self.Balance -= amount 
            return True
    #Return balance
    def balance(self): 
        return self.Balance

    #cash transfer
    def transfer(self, target, amount):
        if(self.Balance - amount < -self.CreditLine):
            return False  
        else: 
            self.Balance -= amount 
            target.Balance += amount 
            return True
 #This demonstrates inheritance       
class MinimumBalanceAccount(Account):
    def __init__(self, minimum_balance):
        Account.__init__(self)
        self.minimum_balance = minimum_balance

    def withdraw(self, amount):
        if self.balance - amount < self.minimum_balance:
            print 'Cant withdraw. Balance is inadquate'
        else:
            Account.withdraw(self, amount)
