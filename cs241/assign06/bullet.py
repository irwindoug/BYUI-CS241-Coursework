class Bullet:
    def __init__(self) -> None:
        pass
    
    def fire(self, angle) -> None:
        print(angle)

    def draw(self) -> None:
        pass

    def alive(self) -> None:
        pass

    def is_off_screen(self, width, height) -> None:
        print (width, height)

    def advance(self) -> None:
        pass

    def test(self) -> int:
        return 2