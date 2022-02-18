from abc import ABC, abstractmethod

class Employee(ABC):
    def __init__(self, name:str) -> None:
        self.name:str = name

    @abstractmethod
    def display(self):
        return NotImplementedError("Subcall must implement abstract method")

    @abstractmethod
    def get_paycheck(self):
        return NotImplementedError("Subcall must implement abstract method")
                
class HourlyEmployee(Employee):
    def __init__(self,name:str, hourly_wage:int, hours:int) -> None:
        super().__init__(name)
        self.hourly_wage:int = hourly_wage
        self.hours:int = hours

    def display(self):
        print (("%s - $%i/hour") % (self.name, self.hourly_wage))

    def get_paycheck(self):
        print(("Paycheck: $%i") % (self.hours * self.hourly_wage))

class SalaryEmployee(Employee):
    def __init__(self, name, salary) -> None:
        super().__init__(name)
        self.salary:int = salary

    def display(self) -> str:
        print (("%s - $%i/year") % (self.name, self.salary))

    def get_paycheck(self):
        print(("Paycheck: $%i") % (self.salary / 24))

def main():
    main_prompt = "Type a letter to enter employee data (H: Hourly | S: Salary) or enter Q to quit:\n"

    employees = []
    employee_type = input(main_prompt).lower()

    # Add employees to list
    while employee_type != 'q':
        print()

        if employee_type == 'h': # Create an hourly employee
            name = input("Enter employee name: ")
            hours = int(input("Enter employee hours: "))
            wage = int(input("Enter employee hourly wage: "))
            employees.append(HourlyEmployee(name, wage, hours))

        elif employee_type == 's': # Create a salary employee
            name = input("Enter employee name: ")
            wage = int(input("Enter employee yearly salary: "))
            employees.append(SalaryEmployee(name, wage))

        else:
            print("Invalid type")
        print()

        employee_type = input(main_prompt).lower()


    # Loop through list of employees and display them
    for employee in employees:
        display_employee_data(employee)

def display_employee_data(employee: Employee) -> None:
    employee.display()
    employee.get_paycheck()

if __name__  == "__main__":
    main()