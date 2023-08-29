# Class CollegeStudent inherits from Student, has method get_college and calculate_fees of Student


class CollegeStudent:
    def __init__(
        self,
        student_name: str,
        student_number: str,
        college: str,
        fees: float,
        enrolment: str,
        total_fee: float,
    ) -> None:
        self.student_name = student_name
        self.student_number = student_number
        self.college = college
        self.fees = fees
        self.enrolment = enrolment
        self.total_fee = total_fee

    def get_student_name(self, student_name: str) -> str:
        # Convert to Sentence case or Title case based on the number of words
        # in the name
        student_name = input("Enter the student name: ")
        if len(student_name.split()) == 1:  # Convert only first word to upper case
            return self.student_name.title()
        else:
            return self.student_name.title()

    def get_student_number(self, student_number: str) -> str:
        # Check if student number is 8 digits long
        while True:
            print("test")
            if not student_number.isnumeric():
                print("Invalid student number, try again.")
            elif not len(student_number) == 8:
                print("Invalid student number, try again.")
            else:
                break
        return self.student_number

    def get_college(self, college: str):
        # Convert to Sentence case or Title case based on the number of words
        # in the name
        college.title()
        return self.college

    def college_fees(self, fees: float):
        # Calculate the fees
        while True:
            if str(fees).isnumeric():
                return self.fees
            else:
                print("Invalid fee, try again.")


class Student(CollegeStudent):
    def __init__(
        self, student_name: str, student_number: str, total_fees: float, courses: dict
    ) -> None:
        self.student_name = student_name
        self.student_number = student_number
        self.total_fees = total_fees
        self.courses = courses

    def add_enrolment(self) -> dict:
        """add_enrolment Return a dictionary of all the courses with their respective fees.


        Args:
            course (str): Name of the course
            fee (int): Cost of the course
        """
        global courses
        courses = {}
        while True:
            continue_adding = input("Would you like to add a course? ")
            # Check if the course name has 4 characters and 4 digits e.g. COMP1000
            if continue_adding.lower() == "yes":
                course = input("Enter the course name: ")
                fee = input("Enter the course fee: ")
                if len(course) == 8 and course[:4].isalpha() and course[4:].isdigit():
                    if fee.isdigit():
                        courses[course] = fee
                    else:
                        print("Invalid fee, try again.")
                else:
                    print("Invalid course name, try again.")
            elif continue_adding.lower() == "no":
                break

        return self.courses

    def __str__(self):
        return f"{self.student_name} ({self.student_number}) is enrolled in {self.college} and pays ${self.fees:.2f} in . He also pays ${self.total_fee:.2f} in course fees."

    def get_total_fees(self, total_fees: float):
        """get_total_fees Return the total fees of the student.

        Returns:
            float: Total fees of the student
        """
        total_fees = 0
        for course in courses:
            # Add the fees of each course to the total fees
            total_fees += float(courses[course])
        return self.total_fees


def main():
    student_name = input("Enter the student name: ")
    student_number = input("Enter the student number: ")
    college = input("Enter the college name: ")
    fees = float(input("Enter the college fees: "))
    total_fee = float(input("Enter the total fees: "))
    student = Student(student_name, student_number, total_fee, courses)
    print(student)


if __name__ == "__main__":
    main()
