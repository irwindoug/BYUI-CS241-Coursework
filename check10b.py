"""
File: sorting.py
Original Author: Br. Burton, designed to be completed by others.
Sorts a list of numbers.
"""


def sort(numbers):
    """
    Fill in this method to sort the list of numbers
    """
    def helper(numlist, first, last):
        if first<last:
            splitpoint = partition(numlist, first, last)

            helper(numlist, first, splitpoint-1)

            helper(numlist, splitpoint+1, last)

    def partition(numlist, first, last):
        pivotvalue = numlist[first]

        leftmark = first+1
        rightmark = last

        done = False
        while not done:

            while leftmark <= rightmark and numlist[leftmark] <= pivotvalue:
                leftmark = leftmark + 1

            while numlist[rightmark] >= pivotvalue and rightmark >= leftmark:
                rightmark = rightmark -1

            if rightmark < leftmark:
                done = True
            
            else:
                temp = numlist[leftmark]
                numlist[leftmark] = numlist[rightmark]
                numlist[rightmark] = temp
                
        temp = numlist[first]
        numlist[first] = numlist[rightmark]
        numlist[rightmark] = temp

        return rightmark
        
    helper(numbers, 0, len(numbers)-1)

def prompt_for_numbers():
    """
    Prompts the user for a list of numbers and returns it.
    :return: The list of numbers.
    """

    numbers = []
    print("Enter a series of numbers, with -1 to quit")

    num = 0

    while num != -1:
        num = int(input())

        if num != -1:
            numbers.append(num)

    return numbers


def display(numbers):
    """
    Displays the numbers in the list
    """
    print("The list is:")
    for num in numbers:
        print(num)


def main():
    """
    Tests the sorting process
    """
    numbers = prompt_for_numbers()
    sort(numbers)
    display(numbers)


if __name__ == "__main__":
    main()
