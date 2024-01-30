
class Student:
    def __init__(self, name, student_id, dob, subject):  # Constructor
        self._name = name  # Instance variable
        self._student_id = student_id  # Instance variable
        self._dob = dob  # Instance variable
        self._subject = subject  # Instance variable

    def get_name(self):  # Getter method
        return self._name

    def set_name(self, new_name):  # Setter method
        self._name = new_name

    def get_student_id(self):  # Getter method
        return self._student_id

# Creating instances of the Student class
student1 = Student("Alice", "001", "1995-02-10", "Biology")
student2 = Student("Bob", "002", "1996-05-12", "Chemistry")

# Communication between objects (calling instance methods)
student1_name = student1.get_name()  # Getting the name of student1
student2.set_name("Robert")  # Changing the name of student2

