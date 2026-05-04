# Base Class
class Department:
    def __init__(self):
        self.dept_id = ""
        self.dept_name = ""

    def getdeptdetails(self):
        self.dept_id = input("Enter Department ID: ")
        self.dept_name = input("Enter Department Name: ")

    def printdept(self):
        print("\n--- Department Details ---")
        print("Department ID:", self.dept_id)
        print("Department Name:", self.dept_name)


# Derived Class (inherits Department)
class Course(Department):
    def __init__(self):
        super().__init__()
        self.code = ""
        self.cname = ""
        self.duration = ""

    def getcourse(self):
        self.code = input("Enter Course Code: ")
        self.cname = input("Enter Course Name: ")
        self.duration = input("Enter Course Duration: ")

    def printcourse(self):
        print("\n--- Course Details ---")
        print("Course Code:", self.code)
        print("Course Name:", self.cname)
        print("Duration:", self.duration)


# Derived Class (inherits Course)
class Student(Course):
    def __init__(self):
        super().__init__()
        self.rollno = ""
        self.sname = ""
        self.mark = ""

    def getdetails(self):
        self.rollno = input("Enter Student Roll No: ")
        self.sname = input("Enter Student Name: ")
        self.mark = input("Enter Student Mark: ")

    def printstudent(self):
        print("\n--- Student Details ---")
        print("Roll No:", self.rollno)
        print("Student Name:", self.sname)
        print("Mark:", self.mark)


# Creating object and accessing all methods
obj = Student()

# Getting input
obj.getdeptdetails()
obj.getcourse()
obj.getdetails()

# Printing all details
obj.printdept()
obj.printcourse()
obj.printstudent()