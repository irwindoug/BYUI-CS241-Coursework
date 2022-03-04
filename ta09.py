class BalanceError(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)

class OutOfChecksError(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)

class CheckingAccount():
    def __init__(self, starting_balance=0, num_checks=0) -> None:
        self.balance: float = starting_balance
        self.check_count: int = num_checks

    def deposit(self, amount) -> None:
        self.balance += amount

    def write_check(self, amount) -> None:
        if amount < 0: raise BalanceError
        if self.check_count <= 0: raise OutOfChecksError

        self.balance -= amount
        self.check_count -= 1

    def display(self) -> None:
        print(("Balance: $%.02f\nChecks Remaining: %i") % (self.balance, self.check_count))

    def apply_for_credit(self, amount) -> None:
        pass

def display_menu():
    """
    Displays the available commands.
    """
    print()
    print("Commands:")
    print("  quit - Quit")
    print("  new - Create new account")
    print("  display - Display account information")
    print("  deposit - Desposit money")
    print("  check - Write a check")


def main():
    """
    Used to test the CheckingAccount class.
    """
    acc = CheckingAccount()
    command = ""

    while command != "quit":
        try:
            display_menu()
            command = input("Enter a command: ")

            if command == "new":
                balance = float(input("Starting balance: "))
                num_checks = int(input("Numbers of checks: "))

                acc = CheckingAccount(balance, num_checks)
            elif command == "display":
                acc.display()
            elif command == "deposit":
                amount = float(input("Amount: "))
                acc.deposit(amount)
            elif command == "check":
                amount = float(input("Amount: "))
                acc.write_check(amount)
            elif command == "credit":
                amount = float(input("Amount: "))
                acc.apply_for_credit(amount)
        
        except OutOfChecksError:
            print('Insufficient checks.')
            command = input('Purchase more checks? (Y/N)').lower()
            if command == 'y':
                acc.check_count += 25
                acc.balance -= 5


if __name__ == "__main__":
    main()