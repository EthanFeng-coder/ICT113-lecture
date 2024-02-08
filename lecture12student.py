class List:
    def __init__(self):
        self._list = []

    def isEmpty(self):
        return len(self._list) == 0

    def append(self, anObject):
        self._list.append(anObject)

# Assuming Student is a class that has been defined
# and s1, s2, s3 are instances of the Student class
s1 = Student(...)
s2 = Student(...)
s3 = Student(...)

# Create an instance of an empty List
list1 = List()

# Check if the list is empty, should return True
print(list1.isEmpty())

# Append student objects to the list
list1.append(s1)
list1.append(s2)
list1.append(s3)

# Check if the list is empty again, should return False
print(list1.isEmpty())