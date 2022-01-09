class NegativeNumberError(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)

def get_inverse(n):

    if (n > 0 ):
        return 1/n
    elif (n == 0):
        raise ZeroDivisionError
    elif (n < 0):
        raise NegativeNumberError
    else:
        raise ValueError

def main():
        try: 
            n = float(input("Enter a number: "))
            print("The result is: %s" % get_inverse(n))
        except ValueError:
            print("Error: The value must be a number")
        except ZeroDivisionError:
            print("Error: Cannot divide by zero")
        except NegativeNumberError:
            print("Error: The value cannot be negative")
    

if __name__== "__main__":
    main()