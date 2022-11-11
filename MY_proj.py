# Create class "Student"
class Student:

    # Constructor
    def __init__(self, course_name, course_code, course_credit, course_prerequisites):
        self.course_name = course_name
        self.course_code = course_code
        self.course_credit = course_credit
        self.course_prerequisites = course_prerequisites

    # Function to create and append new student
    def accept(self, course_name, course_code, course_credit, course_prerequisites):

        # use ' int(input()) ' method to take input from user
        ob = Student(Course_Name, Course_Code, Course_Credit, Course_Prerequisites)
        ls.append(ob)

    # Function to display student details
    def display(self, ob):
        print("Course Name : ", ob.Course_Name)
        print("Course Code: ", ob.Course_Code)
        print("Course Credit : ", ob.Course_Credit)
        print("Course Prerequisites : ", ob.Course_Prerequisites)
        print("\n")

    # Search Function
    def search(self, rn):
        for i in range(ls.__len__()):
            if (ls[i].course_code == rn):
                return i

    # Delete Function
    def delete(self, rn):
        i = obj.search(rn)
        del ls[i]

    # Update Function
    def update(self, rn, No):
        i = obj.search(rn)
        roll = No
        ls[i].rollno = roll


# Create a list to add Students
ls = []
# an object of Student class
obj = Student('', 0, 0, 0)

print("\nOperations used, ")
print("\n1.Add Course details\n2.Add Cousre Code\n3.Search Details of a course\n4.Delete Details of Student\n5.Update Student Details\n6.Exit")


