import gc
import sys

class Employee:
    def __init__(self, emp_id, name, city, state):
        self.emp_id = emp_id
        self.name = name
        self.address = self.Address(city, state)
        print(f"Employee {self.name} hired.")

    class Address:
        def __init__(self, city, state):
            self.city = city
            self.state = state

        def display_address(self):
            print(f"City: {self.city}, State: {self.state}")

    def display_info(self):
        print(f"\nEmployee ID: {self.emp_id}")
        print(f"Name: {self.name}")
        self.address.display_address()


# ---------------- MAIN PROGRAM ----------------

# Enable GC debug
gc.set_debug(gc.DEBUG_STATS)

employees = []   # list to store employee objects

while True:
    print("\n1. Hire Employee")
    print("2. Resign Employee")
    print("3. Display All Employees")
    print("4. Garbage Collector Info")
    print("5. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        emp_id = int(input("Enter Employee ID: "))
        name = input("Enter Name: ")
        city = input("Enter City: ")
        state = input("Enter State: ")

        emp = Employee(emp_id, name, city, state)
        employees.append(emp)

        # Reference count
        print("Reference count:", sys.getrefcount(emp))

    elif choice == 2:
        emp_id = int(input("Enter Employee ID to remove: "))
        for emp in employees:
            if emp.emp_id == emp_id:
                print(f"Employee {emp.name} is resigning...")

                # Reference count before deletion
                print("Reference count before deletion:", sys.getrefcount(emp))

                employees.remove(emp)
                del emp

                # Force garbage collection
                gc.collect()

                print("Employee removed and memory cleaned.")
                break
        else:
            print("Employee not found!")

    elif choice == 3:
        if not employees:
            print("No employees available.")
        else:
            for emp in employees:
                emp.display_info()

    elif choice == 4:
        print("GC Count:", gc.get_count())

    elif choice == 5:
        print("Exiting...")
        break

    else:
        print("Invalid choice!")