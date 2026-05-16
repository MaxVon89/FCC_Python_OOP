import datetime

class BankAccount_US():

    MIN_BALANCE = 100
    CURRENCY = '$'


    def __init__(self, holderName, ammount):
        self.__holderName=holderName
        self.__ammount=ammount


    def isAmountValid(self, val):
        return val>0
    

    def _withdrawMoney(self, val):
        ttype = 'Debit'
        if self.isAmountValid:
            self.__ammount-=val
            print(f"Withdrawn {self.CURRENCY}{val}, new balance: {self.CURRENCY}{self.__ammount}. ")
            self.__transactionLogging(val, ttype)

    def _depositMoney(self, val):
        ttype = 'Creit'
        if self.isAmountValid:
            self.__ammount+=val
            print(f"Deposited {self.CURRENCY}{val}, new balance: {self.CURRENCY}{self.__ammount}. ")
            self.__transactionLogging(val, ttype)


    def __transactionLogging(self, val, ttype):
        print(f"{ttype}ed {self.CURRENCY}{val} at {datetime.time()}")


    @staticmethod
    def isInterestValid(val):
        if 0<=val<=5:
            return True
        return False



#   _____________________
#  |                   |
# |____________________|
myAccount = BankAccount_US('Max', 5000000000)

# myAccount.depositMoney(5000000)
# AttributeError: 'BankAccount_US' object has no attribute 'depositMoney'

myAccount._depositMoney(5000000)

print(BankAccount_US.isInterestValid(3))

# class Customer():
#     MIN_AGE=18
#     NATIONALITY = 'USA'

#     def __init__(self, name, age, nationality, Account):
#         self.name=name
#         self.age=age
#         self.nationality=nationality

    
#     def requestAccountCreation(self, reqAccType)
        