"""
Simple inheritance exercise to demonstrate overriding a method from a superclass.
"""

__copyright__ = "Copyright 2018, University of Queensland"


class Student(object):
    """Simple model of a university student"""

    def __init__(self, name, student_num):
        """
        Parameters:
            name (str): The student's name in "first_name last_name" format.
            student_num (str): The student's unique student id number.
        """
        self._name = name
        self._student_num = student_num
        self._enrolments = []  # list of tuples (course code, tuition fee)

    def get_name(self):
        """(str) Returns the name of the student "first_name last_name"."""

        return self._name.title()

    def get_student_num(self):
        """(str) Returns the students student number."""
        return self._student_num

    def enrol(self, course_code, fee):
        """Enrol in a course, at a given fee.

        Parameters:
            course_code (str): Unique course code in which Student is enrolling.
            fee (int): The fee for taking this course (in whole dollar amount).

        Preconditions:
            fee > 0
        """
        self._enrolments.append((course_code, fee))

    def get_enrolments(self):
        """list<(str, in)> Return a list of courses the student is enrolled in."""
        return self._enrolments

    def calculate_fees(self):
        """Compute the total tuition fees for the student.

        Return:
            int: Total tuition fees for this Student.
        """
        total = 0
        for course_code, fee in self._enrolments:
            total += fee
        return total


# Define your CollegeStudent class here


class CollegeStudent(Student):
    def __init__(self, college, fees, name, student_num):
        super().__init__(name, student_num)
        self.college = college
        self.fees = fees

    def get_college(self):
        """Return the college of the student in title case."""
        return self.college.title()

    def calculate_fees(self):
        """Return the total tuition fees for the student."""
        return super().calculate_fees() + self.fees


def main():
    # Start asking for input
    name = input("Enter student name: ")
    student_num = input("Enter student number: ")
    college = input("Enter college name: ")
    fees = int(input("Enter college fees: "))
    student = CollegeStudent(college, fees, name, student_num)

    print(student.get_college())
    print(student.calculate_fees())
    # Ask for enrol for courses
    while True:
        course_code = input("Enter course code (or blank to finish): ")
        if course_code[:4].isalpha() and course_code[4:].isdigit():
            course_code = course_code.upper()
            fee = int(input("Enter course fee: "))
            student.enrol(course_code, fee)
        elif course_code == "":
            break
        else:
            print("Invalid course code")
    print(student.calculate_fees())
    print(f"Total fees for {student.get_name()} are ${student.calculate_fees()}")


# Start the main
if __name__ == "__main__":
    main()
