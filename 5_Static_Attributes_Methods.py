# """
# ## Static Attributes
# ### Shared datapoints across different instances of a class
# * stored at the class level
# * can be accessed by both instances and classes

# ## Static Methods
#     Methods that belong to a class rather than an instance
#     Cannot access instance-specific data
#     To use, need the '@staticmethod' decorator

# """

# class Users:

#     noOfUsers = 0

#     def __init__(self, username, email):
#         self.__username=username
#         self.__email=email
#         Users.noOfUsers +=1
#         self.userNo = Users.noOfUsers
    
#     def displayUser(self):
#         return f"username: {self.__username}\nemail: {self.__email}"

#     def displayUserNo(self):
#         return f"Your unique user no. is {self.userNo}"

#     def displayNoOfUsers():
#         return Users.noOfUsers
    

#     @staticmethod
#     def getNoOfUsers():
#         return Users.noOfUsers

# e1 = Users('max1', 'max@gmail.com')

# print(e1.displayUser())
# print(e1.displayUserNo(), Users.noOfUsers)

# e2 = Users('ell@', 'ella@gmail.com')

# print(e2.displayUser())
# print(e2.displayUserNo(), Users.noOfUsers)

# print(Users.getNoOfUsers())



class BankAccount_US:
    #Python convention, constants will be all caps
    MIN_BALANCE = 100

    def __init__(self, HolderName, Amount):
        self.HolderName = HolderName
        self.__Amount = Amount
    #instance method
    def deposit(self, val):
        if val>0:
            self.__Amount+=val
            print(f"${val} deposited to {self.HolderName}'s account, new balance is ${self.__Amount}")
        else: print("Invalid amount")


    @staticmethod
    def isInterestValid(val):
        return 0<=val<=5
    


ba2 = BankAccount_US('Monica', 3000000)
ba2.deposit(-2)
ba2.deposit(20000)

print(BankAccount_US.isInterestValid(-1))
print(BankAccount_US.isInterestValid(5))