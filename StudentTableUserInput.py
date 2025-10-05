from prettytable import PrettyTable

# Base class: Student
class Student:
    def __init__(self, reg_no, name):
        self.reg_no = reg_no
        self.name = name

    def display_student(self):
        print(f"Registration No: {self.reg_no}")
        print(f"Name: {self.name}")

# Base class: Exam
class Exam:
    def __init__(self, exam_no, pattern, semester):
        self.exam_no = exam_no
        self.pattern = pattern
        self.semester = semester

    def display_exam(self):
        print(f"Exam No: {self.exam_no}")
        print(f"Pattern: {self.pattern}")
        print(f"Semester: {self.semester}")

# Derived class: Result (inherits from Student and Exam)
class Result(Student, Exam):
    def __init__(self, reg_no, name, exam_no, pattern, semester, physics, chemistry, maths):
        Student.__init__(self, reg_no, name)
        Exam.__init__(self, exam_no, pattern, semester)
        self.physics = physics
        self.chemistry = chemistry
        self.maths = maths

    def display_table_result(self):
        table = PrettyTable()
        table.field_names = ["Field", "Value"]
        table.add_row(["Registration No", self.reg_no])
        table.add_row(["Name", self.name])
        table.add_row(["Exam No", self.exam_no])
        table.add_row(["Pattern", self.pattern])
        table.add_row(["Semester", self.semester])
        table.add_row(["Marks in Physics", self.physics])
        table.add_row(["Marks in Chemistry", self.chemistry])
        table.add_row(["Marks in Maths", self.maths])
        total = self.physics + self.chemistry + self.maths
        average = total / 3
        table.add_row(["Total Marks", total])
        table.add_row(["Average Marks", f"{average:.2f}"])
        print(table)

# Collecting user input
reg_no = input("Enter Registration Number: ")
name = input("Enter Name: ")
exam_no = input("Enter Exam Number: ")
pattern = input("Enter Exam Pattern: ")
semester = input("Enter Semester: ")

# Ensure marks are integers
physics = int(input("Enter Marks in Physics: "))
chemistry = int(input("Enter Marks in Chemistry: "))
maths = int(input("Enter Marks in Maths: "))

# Create Result object and display table
res = Result(reg_no, name, exam_no, pattern, semester, physics, chemistry, maths)
res.display_table_result()
