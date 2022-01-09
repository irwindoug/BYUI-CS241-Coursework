class Student():
    def __init__(self):
        self.first_name = ""
        self.last_name = ""
        self.id_number = 0

def prompt_student(self):
    self.first_name = input("Please enter your first name: ")
    self.last_name = input("Please enter your last name: ")
    self.id_number = int(input("Please enter your id number: "))
    return self.first_name, self.last_name, self.id_number

def display_student(self):
    print ("Your information:")
    print (("%d - %s %s") % (self.id_number, self.first_name, self.last_name))

def main():
    user = Student()
    prompt_student(user)
    print()
    display_student(user)

if __name__ == "__main__":
    main()