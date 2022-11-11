class Course():


    def __init__(self, code='', title='', credit='', prerequisite=''):
        self.code = code
        self.title = title
        self.credit = credit
        self.prerequisite = prerequisite

    def __str__(self):
        # storing last inserted course
        file_name='storeData.txt'
        with open(file_name,'w') as store_info:
            details=(f"course code: {self.code},course name: {self.title}, Total credit: {self.credit}, Prerequisite: {self.prerequisite}\n")
            store_info.write(details)

        return f"course code: {self.code},course name: {self.title}, Total credit: {self.credit}, Prerequisite: {self.prerequisite}"

    def __repr__(self):  # added to represent a class objects as a string
        return self.__str__()