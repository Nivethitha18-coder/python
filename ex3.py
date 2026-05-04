import sys

class Student:
    def __init__(self, rollno, name):
        self.rollno = rollno
        self.name = name
        self.courses = []   # list of course objects
        print(f"Student {self.name} registered.")

    class Course:
        def __init__(self, course_id, course_name):
            self.course_id = course_id
            self.course_name = course_name

        def display_course(self):
            print(f"Course ID: {self.course_id}, Course Name: {self.course_name}")

    def add_course(self, course_id, course_name):
        course = self.Course(course_id, course_name)
        self.courses.append(course)
        print(f"Course '{course_name}' added to {self.name}")

        # Reference counting
        print("Reference count of course:", sys.getrefcount(course))

    def display_details(self):
        print(f"\nStudent Roll No: {self.rollno}")
        print(f"Name: {self.name}")
        print("Enrolled Courses:")

        if not self.courses:
            print("No courses enrolled.")
        else:
            for course in self.courses:
                course.display_course()


# ---------------- MAIN PROGRAM ----------------

students = []

while True:
    print("\n1. Register Student")
    print("2. Add Course to Student")
    print("3. Display Student Details")
    print("4. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        roll = int(input("Enter Roll No: "))
        name = input("Enter Name: ")

        stu = Student(roll, name)
        students.append(stu)

        print("Reference count of student:", sys.getrefcount(stu))

    elif choice == 2:
        roll = int(input("Enter Roll No: "))
        for stu in students:
            if stu.rollno == roll:
                cid = input("Enter Course ID: ")
                cname = input("Enter Course Name: ")
                stu.add_course(cid, cname)
                break
        else:
            print("Student not found!")

    elif choice == 3:
        roll = int(input("Enter Roll No: "))
        for stu in students:
            if stu.rollno == roll:
                stu.display_details()
                break
        else:
            print("Student not found!")

    elif choice == 4:
        print("Exiting program...")
        break

    else:
        print("Invalid choice!")