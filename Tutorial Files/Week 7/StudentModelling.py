class Student(object):
    """Simple representation of a university student."""

    def __init__(self, name, student_num, course_list):
        """Create a student with a name.

        Parameters:
            name (str): The student's name.
        """
        self._name = name
        self._student_num = student_num
        self.course_list = course_list

    def get_name(self):
        """(str) Returns the name of the student."""
        return self._name

    def get_student_num(self):
        """(int) Returns the student number."""
        return self._student_num

    def get_degree(self):
        """(str) Returns the degree of the student."""
        return self.course_list


# Indiviually ask for the student's name, student number and degree
name = input("Enter the student's name: ")
num = int(input("Enter the student's number: "))
degree = input("Enter the student's degree: ")

# Create the student object
student = Student(name, num, degree)

# Ask the user what information they want to know about the student
# Give three options: name, student number and degree
while True:
    info = input("What information would you like to know about the student? ")
    if info == "name":
        print(student.get_name())
    elif info == "student number":
        print(student.get_student_num())
    elif info == "degree":
        print(student.get_degree())
    else:
        print("Invalid input, try again.")
    if input("Would you like to know anything else? ") == "no" or "No":
        break
    elif input("Would you like to know anything else? ") == "yes" or "Yes":
        continue
    elif input("Would you like to know anything else? ") == 0:
        break
    else:
        print("Invalid input, try again.")
