
class Book:
    def __init__(self,book_name,book_No,price):
        self.book_Name=book_name
        self.book_No=book_No
        self.book_Price=price


    def display(self):
        print(f"Book Name:{self.book_Name},Book Num:{self.book_No} ,Book Price:{self.book_Price}")


book1=Book("Atomic Habits",123,420.50)
book2=Book("Deep Work",143,340.20)

book1.display()
book2.display()
