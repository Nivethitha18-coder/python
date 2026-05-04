class employee:
    def __init__(self,name,empid,salary):
      self.name=name
      self.empid=empid
      self.salary=salary
    def display(self):
        print("Name:",self.name)
        print("Employee ID:",self.empid)
        print("Salary:",self.salary)
n=int(input("Enter number of employees :"))
employees=[]
for i in range(n):
        employees=[]
        name=input("Enter your name:")
        empid=int(input("Enter your employee ID:"))
        salary=int(input("Enter your salary:"))
        employees.append(employee(name,empid,salary))
        print("_________EMPLOYEE DETAILS_________")
        for emp in employees:
            emp.display()
search=int(input("ENTER AN ID TO SEARCH:"))
found=0
for emp in employees:
        if search==emp.empid:
            found=1
            emp.display()
            break
        else:
            print("NOT FOUND")
max=employees[0]
for emp in employees:
        if emp.salary>max.salary:
             max=emp
max.display()