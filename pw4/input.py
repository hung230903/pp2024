from domains.student import Student
from domains.course import Course

class Input:
    def input_marks(university):
        student_id = input("Enter the student ID: ")
        for student in university.students:
            if student.student_id == student_id:
                subject = input("Enter the subject: ")
                mark = input("Enter the mark: ")
                student.add_mark(subject, mark)
                break

    def input_students(university):
        num_students = int(input("Enter number of students: "))
        for i in range(num_students):
            name = input("Enter student name: ")
            DoB = input("Enter student DoB: ")
            student_id = input("Enter student ID: ")
            student = Student(name, DoB, student_id)
            university.students.append(student)

    def input_courses(university):
        num_courses = int(input("Enter the number of courses: "))
        for i in range(num_courses):
            name = input("Enter course name: ")
            course = Course(name)
            university.courses.append(course)
