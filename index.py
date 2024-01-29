class Employee:
    def __init__(self, emp_id, name, age, salary):
        self.emp_id = emp_id
        self.name = name
        self.age = age
        self.salary = salary

    def __str__(self):
        return f"{self.emp_id} {self.name} {self.age} {self.salary}"


class EmployeeTable:
    def __init__(self):
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def sort_employees(self, key):
        if key == 1:
            self.employees.sort(key=lambda x: x.age)
        elif key == 2:
            self.employees.sort(key=lambda x: x.name)
        elif key == 3:
            self.employees.sort(key=lambda x: x.salary)
        else:
            print("Invalid sorting parameter. Please choose 1, 2, or 3.")

    def print_table(self):
        for employee in self.employees:
            print(employee)


def main():
    employee_table = EmployeeTable()

    employee_table.add_employee(Employee("161E90", "Ramu", 35, 59000))
    employee_table.add_employee(Employee("171E22", "Tejas", 30, 82100))
    employee_table.add_employee(Employee("171G55", "Abhi", 25, 100000))
    employee_table.add_employee(Employee("152K46", "Jaya", 32, 85000))

    print("Choose sorting parameter:")
    print("1. Age\n2. Name\n3. Salary")

    try:
        sorting_parameter = int(input("Enter the sorting parameter (1, 2, or 3): "))
        employee_table.sort_employees(sorting_parameter)
        print("\nSorted Employee Table:")
        employee_table.print_table()
    except ValueError:
        print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    main()
