class Student:
    def __init__(self, name, DoB, student_id):
        self.name = name
        self.DoB = DoB
        self.student_id = student_id
        self.marks = {} 

    def add_mark(self, subject, mark):
        self.marks[subject] = mark

    def display_info(self):
        print(f"ID: {self.student_id} - Name: {self.name} - DoB: {self.DoB}")
        if self.marks:
            print("Marks: ")
            for subject, mark in self.marks.items():
                print(f"{subject}: {mark}")

class Course:
    def __init__(self, name):
        self.name = name
    
    def display_info(self):
        print(f"Name: {self.name}")

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

    def list_courses(self):
        if not self.courses:
            print("There aren't any courses yet")
        else:
            print("Here is the course list: ")
            for i, course in enumerate(self.courses):
                print(f"{i+1}. ", end = "")
                course.display_info()
    
    def main(self):
        while(True):
            print("""
        --------------------------------
        0. Exit
        1. Input students
        2. Input courses
        3. Input marks
        4. Display students infomation
        5. Display courses
        --------------------------------
        """)
            option = int(input("Your choice: "))                                                         
            if option == 0:
                break
            elif option == 1:
                self.input_students()                                                                            
            elif option == 2:
                self.input_courses()                                                                            
            elif option == 3:
                self.input_marks()                                                                            
            elif option == 4:
                self.list_courses()
            elif option == 5:
                self.list_students()
            else:
                print("Invalid Option. Please try again")

if __name__ == "__main__":
    uni = University()
    uni.main() 