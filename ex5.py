import sys
import gc

class Company:
    def __init__(self, cname):
        self.cname = cname
        self.employees = []   # empty list
        print(f"\nCompany '{self.cname}' created.")

    class Employee:
        def __init__(self, emp_id, emp_name, company):
            self.emp_id = emp_id
            self.emp_name = emp_name
            self.company = company

        def display_details(self):
            print(f"Employee ID: {self.emp_id}, Name: {self.emp_name}, Company: {self.company.cname}")

    def add_employee(self, emp_id, emp_name):
        emp = self.Employee(emp_id, emp_name, self)
        self.employees.append(emp)
        print(f"Employee {emp_name} hired.")

        # Reference count
        print("Employee reference count:", sys.getrefcount(emp))
        print("Company reference count:", sys.getrefcount(self))

    def remove_employee(self, emp_id):
        for emp in self.employees:
            if emp.emp_id == emp_id:
                print(f"Employee {emp.emp_name} is resigning...")

                # Reference count before deletion
                print("Employee ref count before deletion:", sys.getrefcount(emp))

                self.employees.remove(emp)
                del emp

                # Force garbage collection
                gc.collect()

                print("Employee removed and garbage collected.")
                return
        print("Employee not found!")

    def display_all(self):
        if not self.employees:
            print("\nNo employees in the company.")
        else:
            print(f"\nEmployees in {self.cname}:")
            for emp in self.employees:
                emp.display_details()


# ---------------- MAIN PROGRAM ----------------

gc.set_debug(gc.DEBUG_STATS)

# Create company
cname = input("Enter Company Name: ")
comp = Company(cname)

# Number of employees
num_employees = int(input("Enter number of employees to add: "))

# Add employees
for i in range(num_employees):
    print(f"\nEnter details for Employee {i+1}:")
    emp_id = int(input("Enter Employee ID: "))
    emp_name = input("Enter Employee Name: ")
    comp.add_employee(emp_id, emp_name)

# Display all employees
comp.display_all()

# Remove employees
remove_count = int(input("\nEnter number of employees to remove: "))

for i in range(remove_count):
    emp_id = int(input("Enter Employee ID to remove: "))
    comp.remove_employee(emp_id)

# Final display
comp.display_all()

# Final GC info
print("\nGarbage Collector Count:", gc.get_count())
