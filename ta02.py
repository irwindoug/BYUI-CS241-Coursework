def main():
    filename = prompt_filename()
    print(("Opening file '%s'") % filename)

    word = "pride"

    numword = parse_file(filename, word)
    print("The word %s occurs %d times in this file" % (word, numword))

def prompt_filename():
    filename = input("Please enter the filename: ")
    return filename

def parse_file(filename):
    file = open(filename, "r")

    for line in file:
        words = line.split()
        for word in words:
            print(word, end=" ")
        print()
    
    file.close()
