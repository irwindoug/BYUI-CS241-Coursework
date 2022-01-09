'''
Program: Check02b.py
Brother Mellor, CS 241
Author: Doug Irwin
Summary: Checks for lines and words
'''

def main ():
    # Set up initial values
    numwords = 0
    numlines = 0

    # Open and count lines and words from file
    file = open(input("Enter file: "), "r")
    
    # Count lines and words
    for line in file:
        words = line.split()
        numwords += len(words)
        numlines += 1

    # Close file
    file.close()

    # Display count
    print(("The file contains %i lines and %i words.") % (numlines, numwords))

if __name__ == "__main__":
    main()