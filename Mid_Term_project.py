def all_options():

    print("""Choose a number: 
    1. Add a Course
    2. Update a Course
    3. Delete a Course.
    4. Display All course
    5. Individual Course Display
    6. Search A particular Course
    7. store all the data
    0. QUIT""")

import course_functionality
from course import Course

print("Course Management application using Python")
while(True):
    all_options()
    response = int(input())
    if response == 1:
        print("Course Code?")
        code = input()
        print("Course Title?")
        title = input()
        print("Course Credit?")
        credit = input()
        count= True
        while count == True:
            print("Press 1 to add pre requisite and 0 to skip")
            option =int(input('Select an option: '))
            if option==0:
                prerequisite= 0 #setting null value
                count= False
            elif option==1:
                print("Enter Prerequisite: ")
                prerequisite = input()
                count= False
            else:
                print("The optiton is not valid")
                continue
        course_functionality.add_course(Course(code, title, credit, prerequisite))
    elif response == 2:
        print("Current Course code?")
        current_code = input()
        print("Current Course Title?")
        current_title = input()
        print("Current Course Credit?")
        current_credit = input()
        print("current Course prerequisite?")
        current_prerequisite = input()
        print("New course code (s for same)")
        new_code = input()
        if str.lower(new_code) == 's':
            new_code = current_code
        print("New course title (s for same)")
        new_title = input()
        if str.lower(new_title) == 's':
            new_title = current_title
        print("New course credit (s for same)")
        new_credit = input()
        if str.lower(new_credit) == 's':
            new_credit = current_credit
        print("New course prerequisite? (s for same)")
        new_prerequisite = input()
        if str.lower(new_prerequisite) == 's':
            new_prerequisite = current_prerequisite
        course_functionality.update_course(Course(current_code,current_title, current_credit,current_prerequisite),new_code, new_title, new_credit, new_prerequisite)
    elif response == 3:
        print("Enter the course Id to delete?")
        code = input()
        course_functionality.delete_course(Course(code))
    elif response == 4:
        print("Here are all the courses:")
        for course in course_functionality.get_course():
            print(course)
            #stored_courses=course
    elif response == 5:
        print("Enter the individual course Id to search:")
        code = input()
        for course in course_functionality.get_individual_course(Course(code)):
            print(course)
            print("Course Found!!!")
    elif response == 6:
        for course in course_functionality.get_particular_course():
            print("")
    elif response == 7:
        for course in course_functionality.store_course_information():
            print("")
    else:
        print("Application terminated")
        break