class Student(object):
    """Simple representation of a university student."""

    def __init__(
        self,
        first_name: str,
        last_name: str,
        email: str,
        degree: str,
        student_number: str,
    ):
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


# Start asking the user for information
first_name = input("Enter the student's first name: ")
last_name = input("Enter the student's last name: ")
email = input("Enter the student's email: ")
degree = input("Enter the student's degree: ")
number = str(input("Enter the student's number: "))
# Create a student object with the information given
student = Student(first_name, last_name, email, degree, number)
# Ask to either return the string in readable format or python format.
while True:
    format = input(
        "Would you like the information in readable format or python format? "
    )
    if format == 0:
        break
    elif format == "readable":
        print(f"'{first_name} {last_name} ({email}, {degree}, {number})'")
        # Print using class
        print(
            f"'{student.get_first_name()} {student.get_last_name()} ({student.get_email()}, {student.get_degree()}, {student.get_student_number()})'"
        )

    elif format == "python":
        print(
            f"Student('{first_name}', '{last_name}', '{email}', '{degree}', '{number}')"
        )
    else:
        break
