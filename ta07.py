class Employee():
    def __init__(self, name) -> None:
        self.name:str = name

    def display(self) -> str:
        print (self.name)
                
class HourlyEmployee(Employee):
    def __init__(self,name, hourly_wage) -> None:
        super().__init__(name)
        self.hourly_wage:int = hourly_wage

    def display(self):
        print (("%s - $%i/hour") % (self.name, self.hourly_wage))

class SalaryEmployee(Employee):
    def __init__(self, name, salary) -> None:
        super().__init__(name)
        self.salary:int = salary

    def display(self) -> str:
        print (("%s - $%i/year") % (self.name, self.salary))

def main():
    employees = []
    employee_type = input().lower()

    # Add employees to list
    while employee_type != 'q':
        if employee_type == 'h':
            name = input("Name: ")
            wage = int(input("Wage: "))
            hourly_employee = HourlyEmployee(name, wage)
            employees.append(hourly_employee)

        elif employee_type == 's':
            name = input("Name: ")
            wage = int(input("Wage: "))
            salary_employee = SalaryEmployee(name, wage)
            employees.append(salary_employee)

        else:
            print("Invalid type")

        employee_type = input().lower()

    # Loop through list of employees and display them
    for employee in employees:
        employee.display()


if __name__  == "__main__":
    main()