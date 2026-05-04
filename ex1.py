import sys
import gc

class University:
    def __init__(self, university_name):
        self.university_name = university_name
        self.students = []   # list to store student objects

    class Student:
        def __init__(self, rollno, name, university):
            self.rollno = rollno
            self.name = name
            self.university = university

        def display_details(self):
            print(f"Roll No: {self.rollno}, Name: {self.name}, University: {self.university.university_name}")

    def add_student(self, rollno, name):
        student = self.Student(rollno, name, self)
        self.students.append(student)
        print(f"Student {name} added.")

        # Reference count
        print("Reference count of student:", sys.getrefcount(student))

    def remove_student(self, rollno):
        for student in self.students:
            if student.rollno == rollno:
                print(f"Removing student {student.name}...")

                # Show reference count before deletion
                print("Reference count before deletion:", sys.getrefcount(student))

                self.students.remove(student)
                del student

                # Force garbage collection
                gc.collect()

                print("Student removed and garbage collected.")
                return
        print("Student not found!")

    def display_all(self):
        if not self.students:
            print("No students available.")
        else:
            print("\nStudent List:")
            for student in self.students:
                student.display_details()


# ------------------- MAIN PROGRAM -------------------

# Enable garbage collection debugging
gc.set_debug(gc.DEBUG_STATS)

# Create University
uni = University(input("Enter University Name: "))

while True:
    print("\n1. Add Student")
    print("2. Remove Student")
    print("3. Display All Students")
    print("4. Show Garbage Collector Info")
    print("5. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        roll = int(input("Enter Roll No: "))
        name = input("Enter Name: ")
        uni.add_student(roll, name)

    elif choice == 2:
        roll = int(input("Enter Roll No to remove: "))
        uni.remove_student(roll)

    elif choice == 3:
        uni.display_all()

    elif choice == 4:
        print("\nGarbage Collector Counts:", gc.get_count())

    elif choice == 5:
        print("Exiting program...")
        break

    else:
        print("Invalid choice!")