class GPA():
    def __init__(self):
        self.gpa:float = 0

    def get_gpa(self):
        return self.gpa

    def set_gpa(self, gpa):
        if(gpa < 0):
            self.gpa = 0.0
        else:
            self.gpa = gpa

    def get_letter(self):
        if (self.gpa <=.99):
            return "F"
        elif (self.gpa >=1.0 and self.gpa <=1.99):
            return "D"
        elif (self.gpa >= 2.0 and self.gpa <= 2.99):
            return "C"
        elif (self.gpa >= 3.0 and self.gpa <= 3.99):
            return "B"
        elif(self.gpa == 4.0):
            return "A"

    def set_letter(self, letter):
        if (letter == "A"):
            self.gpa = 4.0
        elif(letter == "B"):
            self.gpa = 3.0
        elif(letter == "C"):
            self.gpa = 2.0
        elif(letter == "D"):
            self.gpa = 1.0
        else:
            self.gpa = 0

def main():
    student = GPA()

    print("Initial values:")
    print("GPA: {:.2f}".format(student.get_gpa()))
    print("Letter: {}".format(student.get_letter()))

    gpa = float(input("Enter a new GPA: "))

    student.set_gpa(gpa)

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