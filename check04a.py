class Person():
  def __init__(self):
    self.name = "anonymous"
    self.year = "unknown"
    
  def __str__(self):
    return (("%s (b. %s)") % (self.name, self.year))
  
class Book():
  def __init__(self):
    self.title = "untitled"
    self.author = Person()
    self.publisher = "unpublished"
    
  def __str__(self):
    return (self.title + "\n" + "Publisher:" +"\n" + self.publisher + "\n" + "Author:" + "\n" + str(self.author))

def main():
  book = Book()
  
  print (book)
  print()
  
  print ("Please enter the following:")
  book.author.name = input("Name: ")
  book.author.year = input("Year: ")
  book.title = input("Title: ")
  book.publisher = input("Publisher: ")
  
  print()
  print (book)

if __name__ == "__main__":
  main()