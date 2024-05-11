# Write a Python program to create a person class.
# Include attributes like name, country and date of birth.
# Implement a method to determine the person's age.

class person:
    def __init__(self,name,country):
        self.name=name
        self.country=country
    def display(self):
        print(f" Name:{self.name},Country:{self.country}")

p1=person("Rudra","Berlin")
p1.display()
