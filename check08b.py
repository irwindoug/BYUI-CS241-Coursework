class GPA():
    def __init__(self):
        self._gpa:float = 0


    def _get_gpa(self):
        return self._gpa

    def _set_gpa(self, value):
        if (value > 4):
            self._gpa = 4.0
        elif(value < 0):
            self._gpa = 0.0
        else:
            self._gpa = value

    @property
    def letter(self):
        if (self._gpa <=.99):
            return "F"
        elif (self._gpa >=1.0 and self._gpa <=1.99):
            return "D"
        elif (self._gpa >= 2.0 and self._gpa <= 2.99):
            return "C"
        elif (self._gpa >= 3.0 and self._gpa <= 3.99):
            return "B"
        elif(self._gpa == 4.0):
            return "A"

    @letter.setter
    def letter(self, letter):
        if (letter == "A"):
            self._gpa = 4.0
        elif(letter == "B"):
            self._gpa = 3.0
        elif(letter == "C"):
            self._gpa = 2.0
        elif(letter == "D"):
            self._gpa = 1.0
        else:
            self._gpa = 0

    gpa = property (_get_gpa, _set_gpa)

def main():
    student = GPA()

    print("Initial values:")
    print(("GPA: %.2f") % student.gpa)
    print(("Letter: %s") % (student.letter))

    value = float(input("Enter a new GPA: "))

    student.gpa = value

    print("After setting value:")
    print(("GPA: %.2f") % student.gpa)
    print(("Letter: %s") % (student.letter))

    letter = input("Enter a new letter: ")

    student.letter = letter

    print("After setting letter:")
    print(("GPA: %.2f") % student.gpa)
    print(("Letter: %s") % (student.letter))

if __name__ == "__main__":
    main()
