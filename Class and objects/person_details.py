# Write a Python program to create a person class.
# Include attributes like name, country and date of birth.
# Implement a method to determine the person's age.

from datetime import date
class person:
    def __init__(self,name,country,dob):
        self.name=name
        self.country=country
        self.dob=dob

    def calculate_age(self):
        print(f" Name:{self.name},Country:{self.country}")

        today=date.today()
        age=today.year-self.dob.year
        if(today<date(today.year,self.dob.month,self.dob.day)):
            age-=1
        return age



p1=person("Rudra","Berlin",date(2000,2,10))

p1.calculate_age()
