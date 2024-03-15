from domains.student import Student
from domains.course import Course
import numpy as np

class University:
    def __init__(self):
        self.courses = []
        self.students = []

    def input_marks(self):
        student_id = input("Enter the student ID: ")
        for student in self.students:
            if student.student_id == student_id:
                subject = input("Enter the subject: ")
                mark = input("Enter the mark: ")
                student.add_mark(subject, mark)
                break

    def input_students(self):
        num_students = int(input("Enter number of students: "))
        for i in range(num_students):
            name = input("Enter student name: ")
            DoB = input("Enter student DoB: ")
            student_id = input("Enter student ID: ")
            student = Student(name, DoB, student_id)
            self.students.append(student)

    def input_courses(self):
        num_courses = int(input("Enter the number of courses: "))
        for i in range(num_courses):
            name = input("Enter course name: ")
            course = Course(name)
            self.courses.append(course)

    def list_students(self):
        if not self.students:
            print("There aren't any students yet")
        else:
            print("Here is the student list: ")
            for i, student in enumerate(self.students):
                print(f"{i + 1}. ", end = "")
                student.display_info()
                print("GPA: ", student.gpa())

        self.students.sort(key=lambda x: x.gpa(), reverse=True)
        print("Sorted: ")
        for i, student in enumerate(self.students):
            print(f"{i + 1}. ", end = "")
            student.display_info()

    def list_courses(self):
        if not self.courses:
            print("There aren't any courses yet")
        else:
            print("Here is the course list: ")
            for i, course in enumerate(self.courses):
                print(f"{i+1}. ", end = "")
                course.display_info()
