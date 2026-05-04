class Student:
    def __init__(self, name, roll_no, test_marks):
        self.name = name
        self.roll_no = roll_no
        self.test_marks = test_marks

    def total_marks(self):
        return self.test_marks

    def display(self):
        print(f"Name: {self.name}, Roll No: {self.roll_no}, Test Marks: {self.test_marks}")


class Literary_Student(Student):
    def __init__(self, name, roll_no, test_marks, literary_marks):
        super().__init__(name, roll_no, test_marks)
        self.literary_marks = literary_marks

    def total_marks(self):
        return super().total_marks() + self.literary_marks

    def display(self):
        super().display()
        print(f"Literary Marks: {self.literary_marks}, Total Marks: {self.total_marks()}")


class Sports_Student(Student):
    def __init__(self, name, roll_no, test_marks, sports_marks):
        super().__init__(name, roll_no, test_marks)
        self.sports_marks = sports_marks

    def total_marks(self):
        return super().total_marks() + self.sports_marks

    def display(self):
        super().display()
        print(f"Sports Marks: {self.sports_marks}, Total Marks: {self.total_marks()}")


class Lit_Sport_Student(Student):
    def __init__(self, name, roll_no, test_marks, literary_marks, sports_marks):
        super().__init__(name, roll_no, test_marks)
        self.literary_marks = literary_marks
        self.sports_marks = sports_marks

    def total_marks(self):
        return super().total_marks() + self.literary_marks + self.sports_marks

    def display(self):
        super().display()
        print(f"Literary Marks: {self.literary_marks}, Sports Marks: {self.sports_marks}, Total Marks: {self.total_marks()}")


# Main program
students = []
n = int(input("Enter number of students: "))

for i in range(n):
    print(f"\n--- Enter details for Student {i+1} ---")
    print("Choose student type:")
    print("1. General Student")
    print("2. Literary Student")
    print("3. Sports Student")
    print("4. Literary & Sports Student")

    choice = int(input("Enter choice (1-4): "))

    name = input("Enter name: ")
    roll_no = int(input("Enter roll number: "))
    test_marks = int(input("Enter test marks: "))

    if choice == 1:
        student = Student(name, roll_no, test_marks)

    elif choice == 2:
        literary_marks = int(input("Enter literary marks: "))
        student = Literary_Student(name, roll_no, test_marks, literary_marks)

    elif choice == 3:
        sports_marks = int(input("Enter sports marks: "))
        student = Sports_Student(name, roll_no, test_marks, sports_marks)

    elif choice == 4:
        literary_marks = int(input("Enter literary marks: "))
        sports_marks = int(input("Enter sports marks: "))
        student = Lit_Sport_Student(name, roll_no, test_marks, literary_marks, sports_marks)

    else:
        print("Invalid choice! Skipping this student.")
        student = None

    if student:
        students.append(student)

print("\n===== Student Report =====")
for student in students:
    student.display()
    print("-" * 40)