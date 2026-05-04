class Employee:
    def __init__(self, emp_id, name, salary, percentage):
        self.emp_id = emp_id
        self.name = name
        self.salary = salary
        self.percentage = percentage

    def calculate_bonus(self):
        return (self.salary * self.percentage) / 100

    def display(self):
        print(f"ID: {self.emp_id}, Name: {self.name}, Salary: {self.salary}, Bonus: {self.calculate_bonus()}")


class Manager(Employee):
    def __init__(self, emp_id, name, salary, percentage, department, team_size, allowance):
        super().__init__(emp_id, name, salary, percentage)
        self.department = department
        self.team_size = team_size
        self.allowance = allowance

    def manager_details(self):
        return f"Department: {self.department}, Team Size: {self.team_size}, Allowance: {self.allowance}"

    def printManager(self):
        self.display()
        print(self.manager_details())


class Developer(Employee):
    def __init__(self, emp_id, name, salary, percentage, project, experience):
        super().__init__(emp_id, name, salary, percentage)
        self.project = project
        self.experience = experience

    def developer_details(self):
        return f"Project: {self.project}, Experience: {self.experience} years"

    def printDeveloper(self):
        self.display()
        print(self.developer_details())


# Main program
employees = []
n = int(input("Enter number of employees: "))

for i in range(n):
    print(f"\n--- Enter details for Employee {i+1} ---")
    print("Choose employee type:")
    print("1. General Employee")
    print("2. Manager")
    print("3. Developer")

    choice = int(input("Enter choice (1-3): "))

    emp_id = int(input("Enter Employee ID: "))
    name = input("Enter name: ")
    salary = float(input("Enter salary: "))
    percentage = float(input("Enter bonus percentage: "))

    if choice == 1:
        employee = Employee(emp_id, name, salary, percentage)

    elif choice == 2:
        department = input("Enter department: ")
        team_size = int(input("Enter team size: "))
        allowance = float(input("Enter allowance: "))
        employee = Manager(emp_id, name, salary, percentage, department, team_size, allowance)

    elif choice == 3:
        project = input("Enter project name: ")
        experience = int(input("Enter years of experience: "))
        employee = Developer(emp_id, name, salary, percentage, project, experience)

    else:
        print("Invalid choice! Skipping this employee.")
        employee = None

    if employee:
        employees.append(employee)

print("\n===== Employee Report =====")
for emp in employees:
    if isinstance(emp, Manager):
        emp.printManager()
    elif isinstance(emp, Developer):
        emp.printDeveloper()
    else:
        emp.display()
    print("-" * 40)