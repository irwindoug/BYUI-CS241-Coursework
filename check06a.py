'''
Program: Check06a.py
Brother Mellor, CS 241
Author: Doug Irwin
Purpose: Write programs that correctly use inheritance to solve problems.
'''

class Book():
    def __init__(self):
        self.title = ""
        self.author = ""
        self.publication_year = 0

    def prompt_book_info(self):
        self.title = input("Title: ")
        self.author = input("Author: ")
        self.publication_year = int(input("Publication Year: "))

    def display_book_info(self):
        print(("%s (%i) by %s") % (self.title, self.publication_year, self.author))


class TextBook(Book):
    def __init__(self):
        super().__init__()
        self.subject = ""

    def prompt_subject(self):
        self.subject = input("Subject: ")

    def display_subject(self):
        print(("Subject: %s") % self.subject)

class PictureBook(Book):
    def __init__(self):
        super().__init__()
        self.illustrator = ""

    def prompt_illustrator(self):
        self.illustrator = input("Illustrator: ")

    def display_illustrator(self):
        print(("Illustrated by %s") % self.illustrator)

def main():
    book = Book()
    textbook = TextBook()
    picturebook = PictureBook()

    book.prompt_book_info()
    print()
    book.display_book_info()

    print()

    textbook.prompt_book_info()
    textbook.prompt_subject()
    print()
    textbook.display_book_info()
    textbook.display_subject()

    print()

    picturebook.prompt_book_info()
    picturebook.prompt_illustrator()
    print()
    picturebook.display_book_info()
    picturebook.display_illustrator()

if __name__ == "__main__":
    main()