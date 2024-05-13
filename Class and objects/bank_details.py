

class Bank:
    def __init__(self,account_num,account_name,balance):
        self.accountNum=account_num
        self.accountName = account_name
        self.avaBal=balance

    def create_acc(self):
        if self.accountNum==123456:
            print("already created! Create new account Number")
        else:
            print("new account")
    def balance_acc(self):
        if self.avaBal<=100:
            print ("withdraw")
        else:
            print("insufficent balance")


    def display(self):
       print (f"Account Number :{self.accountNum},Account Name :{self.accountName}")


b1=Bank(123456,"Rudra",150)
b1.display()
b1.balance_acc()
b1.create_acc()