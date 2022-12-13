class BankAccount:
    def __init__(self,holder,accno,balance):
        self.holder=holder
        self.accno=accno
        self.balance=balance
    def deposit(self,amount):
        self.balance+=amount
       
    def withdraw(self,amount):
        if amount<=self.balance:
            self.balance-=amount
               
        else:
            print("Insufficient Amount")
            
    def print_passbook(self):
        return f"BankAccount Details: name:{self.holder},acc_no:{self.accno},Curr_balance:{self.balance}"
           
    def __str__(self):
        return f"BankAccount {self.holder},{self.accno},{self.balance}"
