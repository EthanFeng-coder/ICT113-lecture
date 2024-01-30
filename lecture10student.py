class Student:
    def __init__(self, name, student_id, date_of_birth, subject):
        self.name = name
        self.student_id = student_id
        self.date_of_birth = date_of_birth
        self.subject = subject

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_student_id(self):
        return self.student_id

    def set_student_id(self, student_id):
        self.student_id = student_id

    def get_date_of_birth(self):
        return self.date_of_birth

    def set_date_of_birth(self, date_of_birth):
        self.date_of_birth = date_of_birth

    def get_subject(self):
        return self.subject

    def set_subject(self, subject):
        self.subject = subject

    def display_data(self):
        print(f"Student Name: {self.name}")
        print(f"Student ID: {self.student_id}")
        print(f"Date of Birth: {self.date_of_birth}")
        print(f"Subject: {self.subject}")

# Creating a new student object
new_student = Student("Jane Doe", "S123456", "1990-01-01", "Computer Science")

# Displaying the student's data
new_student.display_data()

# Updating and getting the student's name
new_student.set_name("John Doe")
print(new_student.get_name())

# Updating the student's ID
new_student.set_student_id("S654321")

# Getting the new student ID
print(new_student.get_student_id())

# Updating the student's date of birth
new_student.set_date_of_birth("1992-02-02")

# Getting the new date of birth
print(new_student.get_date_of_birth())

# Updating the student's subject
new_student.set_subject("Mathematics")

# Getting the new subject
print(new_student.get_subject())

# Finally, display all the updated data
new_student.display_data()