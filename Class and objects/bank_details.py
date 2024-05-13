

class Bank:
    def __init__(self,account_num,account_name):
        self.accountNum=account_num
        self.accountName = account_name

    def display(self):
       print (f"Account Number :{self.accountNum},Account Name :{self.accountName}")


b1=Bank(45353535,"Rudra")
b1.display()