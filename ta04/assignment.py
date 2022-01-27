from date import Date

class Assignment():
    def __init__(self):
        self.name = "Untitled"
        self.start_date = Date()
        self.due_date = Date()
        self.end_date = Date()

    def prompt(self):
        self.name = input("Name: ")
        print("\n"+"Start Date:")
        self.start_date.prompt()
        print("\n"+"Due Date:")
        self.due_date.prompt()
        print("\n"+"End Date:")
        self.end_date.prompt()

    def display(self):
        print("Assignment: "+ self.name + "\n" + "Start Date:" + "\n" + self.start_date.display() + "\n" + "Due Date:" + "\n" + self.due_date.display() + "\n" + "End Date:" + "\n" + self.end_date.display())
