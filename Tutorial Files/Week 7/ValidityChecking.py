import time


class Student(object):
    """Simple Representation of a University Student."""

    def __init__(self, first_name, last_name, email, degree, student_number) -> None:
        """Create a student with a name.

        Parameters:
            name (str): The student's name.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.degree = degree
        self.student_number = student_number

    def get_first_name(self):
        """(str) Returns the first name of the student."""
        return self.first_name

    def get_last_name(self):
        """(str) Returns the last name of the student."""
        return self.last_name

    def get_email(self):
        """(str) Returns the email of the student."""
        return self.email

    def get_degree(self):
        """(str) Returns the degree of the student."""
        return self.degree

    def get_student_number(self):
        """(int) Returns the student number of the student."""
        return self.student_number


# Make a list of students to store all the students
students = []

num_students = int(input("How many students would you like to add? "))
for i in range(num_students):
    first_name = input("Enter the student's first name: ")
    last_name = input("Enter the student's last name: ")
    email = input("Enter the student's email: ")
    degree = input("Enter the student's degree: ")
    number = str(input("Enter the student's number: "))
    list.append(students, Student(first_name, last_name, email, degree, number))

# Ask whether to see the list
list = input("Would you like to see the list of students? ")
if list == "yes" or list == "y" or list == "Y":
    print(students)
else:
    if list == "no" or list == "n" or list == "N":
        print("Okay, moving on...")
        time.sleep(2)

# Check if any student number is the same/duplicate
print("Checking for duplicate student numbers...")
time.sleep(5)
# Check for duplicate student numbers
# If numbers are the same, return the student names

# TODO: Check for duplicate student numbers

# Ask the user for a student number to check
print("Which student number would you like to check?")
student_number = input("Enter the student number: ")
print("Checking for duplicate student numbers...")
