'''
Program: Check06b.py
Brother Mellor, CS 241
Author: Doug Irwin
Purpose: Write programs that correctly use inheritance to solve problems.
'''

class Phone():
    def __init__(self):
        self.area_code = 0
        self.prefix = 0
        self.suffix = 0

    def prompt_number (self):
        self.area_code = int(input("Area Code: "))
        self.prefix = int(input("Prefix: "))
        self.suffix = int(input("Suffix: "))

    def display(self):
        print(("(%3i)%3i-%4i") % (self.area_code, self.prefix, self.suffix))

class SmartPhone(Phone):
    def __init__(self):
        super().__init__()
        self.email = ""

    def prompt(self):
        self.prompt_number()
        self.email = input("Email: ")

    def display(self):
        super().display()
        print(("%s") % self.email)

def main():
    phone = Phone()
    smartphone = SmartPhone()

    print("Phone:")
    phone.prompt_number()
    print("\n"+"Phone info:")
    phone.display()

    print("\n" + "Smart phone:")
    smartphone.prompt()
    print("\n" + "Phone info:")
    smartphone.display()    

if __name__ == "__main__":
    main()