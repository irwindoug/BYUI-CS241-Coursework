'''
check02a
Brother Mellow, CS 241

Doug Irwin
'''

def main():
    num1 = prompt_number()
    num2 = prompt_number()
    num3 = prompt_number()
    sum = compute_sum(num1,num2, num3)

    print(("The sum is: %i") % sum)

def prompt_number():
    number = int(input("Enter a positive number: "))
    while number < 0:
        print("Invalid entry. The number must be positive.")
        number = int(input("Enter a positive number: "))
    print()
    return number

def compute_sum(num1, num2, num3):
    return num1 + num2 + num3

if __name__ == "__main__":
    main()