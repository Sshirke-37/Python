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
        # Initialize both base classes
        Student.__init__(self, reg_no, name)
        Exam.__init__(self, exam_no, pattern, semester)
        self.physics = physics
        self.chemistry = chemistry
        self.maths = maths

    def display_result(self):
        self.display_student()
        self.display_exam()
        print(f"Marks in Physics: {self.physics}")
        print(f"Marks in Chemistry: {self.chemistry}")
        print(f"Marks in Maths: {self.maths}")
        total = self.physics + self.chemistry + self.maths
        average = total / 3
        print(f"Total Marks: {total}")
        print(f"Average Marks: {average:.2f}")

# Sample usage
res = Result("S123", "Soham", "EX456", "MCQ", "5th", 85, 90, 88)
res.display_result()
