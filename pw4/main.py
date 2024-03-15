from domains.university import University
from output import Output
from input import Input

if __name__ == "__main__":
        uni = University()
        while(True):
            print("""
        --------------------------------
        0. Exit
        1. Input students
        2. Input courses
        3. Input marks
        4. Display students information
        5. Display courses
        --------------------------------
        """)
            option = int(input("Your choice: "))                                                         
            if option == 0:
                break
            elif option == 1:
                uni.input_students()                                                                            
            elif option == 2:
                uni.input_courses()                                                                            
            elif option == 3:
                uni.input_marks()                                                                            
            elif option == 4:
                uni.list_students()
            elif option == 5:
                uni.list_courses()
            else:
                print("Invalid Option. Please try again")
