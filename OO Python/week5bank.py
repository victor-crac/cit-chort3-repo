from ast import Str
from unicodedata import name
# from unicodedata import name


class BankAccount:
    def __init__(self ,accountNumber,balance,owner,type) -> None:
    
     self.a =accountNumber 
     self.b =balance
     self.owner =owner
     self.type =type
    def __str__(self) -> str:
        return 'the {} account is a {} type of account, is owned by {} and has a balance of {} '.format(self.a,self.type,self.owner,self.b)

class Bank:
    def __init__(self ,name , accounts) -> None:
        self.name = name
        self.accounts = accounts

    def bankAccount(self ,b):
         self.bankAccount.append(b)

    def __repr__(self) -> str:
          return f'This  is {self.name} bank'

class Customer:
    def __init__(self , name , accounts) -> None:
        self.name =name
        self.accounts = accounts

    def addBankAccount(self ,b):
         self.bankAccount.append(b)

    def __repr__(self) -> str:
        return f'Hello {self.name}'
class Transaction:
    def __init__(self , account ,amount ,type) -> None:

# print(customer_A)
        self.amount =amount
        self.type=type

equity = Bank('EQUITY BANK' , accounts=[])
customer_A =Customer('MUSINGUZI DOUGLAS' , accounts=[])
bank =BankAccount('de0992872' ,546567 , 'Douglas' , 'Fixed DEposit')
# print(equity)
# print(customer_A)
print(customer_A.__repr__())
print(equity.__repr__())
print(bank.__str__())

def create_bank(name,accounts,bank_obj):
    bank_obj = Bank(name)
    for account in accounts:
        bank_obj.addBankAccounts(account)
    return bank_obj

# Creting new customer object

def create_customer(name,accounts,cust_obj):
    cust_obj = Bank(name)
    for account in accounts:
        cust_obj.addBankAccounts(account)

# new bankAccount object

def create_BankAccount(accountNumber,balance,owner,type,bankAcc_obj):
    bankAcc_obj = BankAccount(accountNumber,balance,owner,type)

# create a transaction object

def create_Transaction(amount,type,account,trans_obj,bankAcc_obj):
    trans_obj = Transaction(amount,type)
    trans_obj.add_account(create_BankAccount)


   


        
       
       