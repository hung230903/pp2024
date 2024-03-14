def input_something(args):
    return int(input(f"Enter the number of {args} in this class: "))

def input_infos(args):
    item = {"mark": {}}
    if args == "students":
        item["name"] = input("Enter student name: ")
        item["DoB"] = input("Enter student DoB: ")
        item["id"] = input("Enter student ID: ")
    elif args == "courses":
        item["name"] = input("Enter course name: ")
    return item

def input_mark(student):
    subject = input("Enter subject: ")
    mark = input("Enter mark: ")
    student["mark"][subject] = mark

def list_students(students):
    if len(students) == 0:
        print("There aren't any students yet")
    else:
        print("Here is the student list: ")
        for i, student in enumerate(students):
            print(f"{i + 1}. {student['id']} - {student['name']} - {student['DoB']}")
            if "marks" in student:
                print("Marks (Course Id - Mark): ", end = "")   
                for subject, mark in student["mark"].items():
                    print(f"{subject}: {mark}", end = "")
                print()

def list_courses(courses):
    if len(courses) == 0:
        print("There aren't any courses yet")
    else:
        print("Here is the course list: ")
        for i, course in enumerate(courses):
            print(f"{i+1}. {course['name']}")
        
def main():
    courses = []
    students = []
    num_students = 0
    num_courses = 0

    while(True):
        print("""
    --------------------------------
    0. Exit
    1. Input students
    2. Input courses
    3. Input marks
    4. Display students infomation
    5. Display courses
    """)
        option = int(input("Your choice: "))                                                         
        if option == 0:
            break
        elif option == 1:                                                                            
            num_students = input_something("students")
            for i in range(num_students):
                students.append(input_infos("students"))
        elif option == 2:                                                                                                                                 
            num_courses = input_something("courses")
            for i in range(num_courses):
                courses.append(input_infos("courses"))
        elif option == 3:
            student_id = input("Enter student id: ")
            for student in students:
                if student["id"] == student_id:
                    input_mark(student)
                    break                                                                            
        elif option == 4:
            list_students(students)
        elif option == 5:
            list_courses(courses)
        else:
            print("Invalid Option. Please try again")

if __name__ == "__main__":
    main()