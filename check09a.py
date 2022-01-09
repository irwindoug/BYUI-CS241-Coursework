def main():
    valid_input = False

    while not valid_input:
        try: 
            n = int(input("Enter a number: "))
            valid_input = True
        except ValueError:
            print("The value entered is not valid")

    print("The result is: %d" % (n * 2))


if __name__ == "__main__":
    main()