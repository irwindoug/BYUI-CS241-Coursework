from employee import Employee

class HourlyEmployee(Employee):
    def __init__(self):
        super().__init__()
        self.hourly_wage = 0
        self.hours = 0

    def display(self):
        print(("%s - $%i/hour") % (self.name, self.hourly_wage))

class SalaryEmployee(Employee):
    def __init__(self):
        super().__init__()
        self.salary = 0

    def display(self):
        print(("%s - $%i/year") % (self.name, self.salary))

class main():
    employees = []

    user_input = input("h (hourly) | s (salary) | q (quit)")

    while(user_input != "q" and user_input != "Q"):
        if(user_input == "h" or user_input == "H"):
            employee = HourlyEmployee()

            employee.name = input("Enter employee name: ")
            employee.hourly_wage = int(input("Enter hourly wage: $"))

            employees.append(employee)

        elif(user_input == "s" or user_input == "S"):
            employee = SalaryEmployee()

            employee.name = input("Enter employee name: ")
            employee.salary = int(input("Enter annual salary: $"))

            employees.append(employee)
        
        print()
        
        user_input = input("h (hourly) | s (salary) | q (quit)")

    for employee in employees:
        employee.display()

if __name__ == "__main__":
    main()