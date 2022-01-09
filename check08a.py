class GPA():
    def __init__(self):
        self.value = 0

    def get_gpa(self):
        return self.value

    def set_gpa(self, value):
        if (value > 4):
            self.value = 4.0
        elif(value < 0):
            self.value = 0.0
        else:
            self.value = value

    def get_letter(self):
        if (self.value <=.99):
            return "F"
        elif (self.value >=1.0 and self.value <=1.99):
            return "D"
        elif (self.value >= 2.0 and self.value <= 2.99):
            return "C"
        elif (self.value >= 3.0 and self.value <= 3.99):
            return "B"
        elif(self.value == 4.0):
            return "A"

    def set_letter(self, letter):
        if (letter == "A"):
            self.value = 4.0
        elif(letter == "B"):
            self.value = 3.0
        elif(letter == "C"):
            self.value = 2.0
        elif(letter == "D"):
            self.value = 1.0
        else:
            self.value = 0

def main():
    student = GPA()

    print("Initial values:")
    print("GPA: {:.2f}".format(student.get_gpa()))
    print("Letter: {}".format(student.get_letter()))

    value = float(input("Enter a new GPA: "))

    student.set_gpa(value)

    print("After setting value:")
    print("GPA: {:.2f}".format(student.get_gpa()))
    print("Letter: {}".format(student.get_letter()))

    letter = input("Enter a new letter: ")

    student.set_letter(letter)

    print("After setting letter:")
    print("GPA: {:.2f}".format(student.get_gpa()))
    print("Letter: {}".format(student.get_letter()))

if __name__ == "__main__":
    main()
