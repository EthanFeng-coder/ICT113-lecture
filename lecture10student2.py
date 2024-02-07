
class Student:
    def __init__(self, name, student_id, dob, subject):
        # Instance variables
        self.name = name
        self.student_id = student_id
        self.dob = dob
        self.subject = subject

    # Instance method to display student information
    def display_info(self):
        print(f"Student Name: {self.name}")
        print(f"Student ID: {self.student_id}")
        print(f"Date of Birth: {self.dob}")
        print(f"Subject: {self.subject}")

# The main function
def main():
    # Creating an object of the Student class
    student1 = Student("John Doe", "A001", "2000-01-01", "Mathematics")
    # Using the object's method to display its information
    student1.display_info()

# The conditional to ensure main() runs when script is executed directly
if __name__ == "__main__":
    main()

