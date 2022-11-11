from course import Course
import sqlite3
import os.path

l = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

conn = sqlite3.connect(os.path.join(l, 'courses.db'))

c = conn.cursor()
# Creating table if not exist
c.execute('''CREATE TABLE IF NOT EXISTS courses
             (code INTEGER, title TEXT, credit INTEGER, prerequisite INTEGER)''')


def cursor():
    l = os.path.realpath(
        os.path.join(os.getcwd(), os.path.dirname(__file__)))
    return sqlite3.connect(os.path.join(l, 'courses.db')).cursor()


def add_course(course):
    c = cursor()
    with c.connection:
        c.execute("INSERT INTO courses VALUES (?, ?, ?, ?)", (course.code, course.title, course.credit,course.prerequisite))
    c.connection.close()
    return c.lastrowid


def get_course_by_title(title):
    c = cursor()
    c.execute('SELECT * FROM courses WHERE title=?', (title,))
    data = c.fetchone()
    c.connection.close()
    if not data:
        return None
    return Course(data[0], data[1])


def get_course():
    c = cursor()
    courses = []
    for row in c.execute('SELECT * FROM courses'):
        courses.append(Course(row[0], row[1], row[2], row[3]))
    c.connection.close()
    return courses

def store_course_information():
    c = cursor()
    courses = []
    for row in c.execute('SELECT * FROM courses'):
        courses.append(Course(row[0], row[1], row[2], row[3]))
    c.connection.close()
    with open('store_data_from_function.txt','w') as info:
        info.write(str(courses))
    print("All information stored in txt file")
    return courses


def get_individual_course(course):
    c = cursor()
    courses = []
    for row in c.execute('SELECT * FROM courses WHERE code=?',(course.code)):
        courses.append(Course(row[0], row[1], row[2], row[3]))
    c.connection.close()
    return courses

def get_particular_course():
    c = cursor()
    courses = []
    for row in c.execute('SELECT * FROM courses'):
        courses.append(Course(row[0], row[1], row[2], row[3]))
    c.connection.close()
    search = input("Please Enter A Course Name to search: ")
    if search in courses:
        print("The Course Is Found. That Is: ", courses.index(search))
    else:
        print("Not found")
    return courses

def update_course(course,new_code,new_title,new_credit,new_prerequisite):
    c = cursor()
    with c.connection:  # don't forget this part.
        c.execute('UPDATE courses SET code=?, title=?, credit=?,prerequisite=?  WHERE code=? AND title=? AND credit=? AND prerequisite=?',
                  (new_code,new_title,new_credit,new_prerequisite, course.code, course.title,course.credit,course.prerequisite))
    course = get_course_by_title(course.title)  # after commit
    c.connection.close()
    return course


def delete_course(course):
    c = cursor()
    with c.connection:
        c.execute('DELETE FROM courses WHERE code=?', (course.code))
    rows = c.rowcount
    c.connection.close()
    return rows

