from ast import Str
from unicodedata import name


class BankAccount:
    def __init__(self ,acccountNumber,balance,owner,type) -> None:
    
     self.a =acccountNumber 
     self.b =balance
     self.owner =owner
     self.type =type
    
    def __repr__(self) -> str:
        f'This A/C NO{a} with balance of {} is a {} and owned by {}'

class Bank:
    def __init__(self ,name , accounts) -> None:
        self.name = name
        self.accounts = accounts

    def bankAccount(self ,b):
         self.bankAccount.append(b)

    def __repr__(self) -> str:
        f'This  is {name} bank'

class Customer:
    def __init__(self , name , accounts) -> None:
        self.customerName =name
        self.accounts = accounts

    def bankAccount(self ,b):
         self.bankAccount.append(b)

    def __repr__(self) -> str:
        f'Hello {name}'
class Transaction:
    def __init__(self , account ,amount ,type) -> None:

        self.account=account
        self.amount =amount
        self.type=type

equity = Bank('EQUITY BANK' , accounts=[])
customer_A =Customer('MUSINGUZI DOUGLAS' , accounts=[])
bankAccount =BankAccount('de0992872' ,'546567' , 'Douglas' , 'Fixed DEposit')



        
       
       