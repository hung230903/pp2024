class Output:
    def list_students(university):
        if not university.students:
            print("There aren't any students yet")
        else:
            print("Here is the student list: ")
            for i, student in enumerate(university.students):
                print(f"{i + 1}. ", end = "")
                student.display_info()
                print("GPA: ", student.gpa())

        university.students.sort(key = lambda x: x.gpa(), reverse = True)
        print("Sorted: ")
        for i, student in enumerate(university.students):
            print(f"{i + 1}. ", end = "")
            student.display_info()

    def list_courses(university):
        if not university.courses:
            print("There aren't any courses yet")
        else:
            print("Here is the course list: ")
            for i, course in enumerate(university.courses):
                print(f"{i+1}. ", end = "")
                course.display_info()
