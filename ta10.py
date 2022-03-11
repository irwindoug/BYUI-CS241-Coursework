"""
File: ta10-solution.py
Author: Br. Burton
This file demonstrates the merge sort algorithm. There
are efficiencies that could be added, but this approach is
made to demonstrate clarity.
"""

from random import randint
MAX_NUM = 100


def merge_sort(items):
    """
    Sorts the items in the list
    :param items: The list to sort
    """

    # If list is 0 or 1, exit
    if len(items) <= 1:
        return

    # Split lists in 2
    middle = len(items) // 2
    part1 = items[:middle]
    part2 = items[middle:]

    i = 0
    j = 0
    k = 0

    merge_sort(part1)
    merge_sort(part2)

    while i < len(part1) and j < len(part2):
        if part1[i] < part2[j]:
            items[k] = part1[i]
            i +=1
        else:
            items[k] = part2[j]
            j += 1
        k += 1

    while i < len(part1):
        items[k] = part1[i]
        i += 1
        k += 1

    while j < len(part2):
        items[k] = part2[j]
        j += 1
        k += 1



def generate_list(size):
    """
    Generates a list of random numbers.
    """
    items = [randint(0, MAX_NUM) for i in range(size)]
    return items


def display_list(items):
    """
    Displays a list
    """
    for item in items:
        print(item)


def main():
    """
    Tests the merge sort
    """
    size = int(input("Enter size: "))

    items = generate_list(size)
    merge_sort(items)

    print("\nThe Sorted list is:")
    display_list(items)


if __name__ == "__main__":
    main()