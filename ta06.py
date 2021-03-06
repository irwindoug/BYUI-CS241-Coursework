class Point():
    def __init__(self):
        self.x = 0
        self.y = 0

    def prompt_for_point(self):
        self.x = float(input("Enter x: "))
        self.y = float(input("Enter y: "))

    def display(self):
        print(("(%s, %s)") % (self.x, self.y))

class Circle(Point):
    def __init__(self):
        super().__init__()
        self.radius = 0

    def prompt_for_circle(self):
        self.prompt_for_point()
        self.radius = float(input("Enter radius: "))

    def display(self):
        print("Center:")
        super().display()
        print(("Radius: %s") % (self.radius))


def main():
    circle = Circle()

    circle.prompt_for_circle()
    circle.display()

if __name__ == "__main__":
    main()