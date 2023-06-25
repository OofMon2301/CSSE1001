class Course:
    def __init__(self, name, units, weightage):
        self.name = name
        self.units = units
        self.weightage = weightage
        self.assignments = []
        self.grades = []

    def add_assignment(self, weightage):
        self.assignments.append(weightage)

    def add_grade(self, grade):
        self.grades.append(grade)


def calculate_gpa(grades, weightages):
    total_grade = sum(grade * weightage for grade, weightage in zip(grades, weightages))
    total_weightage = sum(weightages)
    if total_weightage == 0:
        return 0
    else:
        return total_grade / total_weightage


def calculate_course_grade(course):
    gpa = calculate_gpa(course.grades, course.assignments)
    percentage = (gpa / 7) * 100
    return gpa, percentage


def calculate_overall_grade(courses):
    overall_percentage = 0
    overall_gpa = 0
    for course in courses:
        gpa, percentage = calculate_course_grade(course)
        overall_gpa += gpa
        overall_percentage += percentage
    overall_gpa /= len(courses)
    overall_percentage /= len(courses)
    return overall_gpa, overall_percentage


def display_dashboard(courses):
    print("----- Dashboard -----")
    for course in courses:
        gpa, percentage = calculate_course_grade(course)
        print(f"Course: {course.name}")
        print(f"Units: {course.units}")
        print(f"Weightage: {course.weightage}")
        print(f"GPA: {gpa}")
        print(f"Percentage: {percentage}%")
        print("----------------------")


def get_grade(score):
    if score < 20:
        return 1
    elif 20 <= score < 45:
        return 2
    elif 45 <= score < 50:
        return 3
    elif 50 <= score < 65:
        return 4
    elif 65 <= score < 75:
        return 5
    elif 75 <= score < 85:
        return 6
    else:
        return 7


def main():
    name = input("Enter your name: ")
    num_courses = int(input("Enter the number of courses you study: "))

    courses = []
    for _ in range(num_courses):
        course_name = input("Enter course name: ")
        course_units = int(input("Enter number of units for the course: "))
        course_weightage = float(input("Enter weightage for the course: "))

        course = Course(course_name, course_units, course_weightage)

        num_assignments = 4  # Assuming each course has 4 assignments
        for _ in range(num_assignments):
            assignment_weightage = float(input("Enter assignment weightage: "))
            course.add_assignment(assignment_weightage)

        courses.append(course)

    display_dashboard(courses)

    for course in courses:
        print(f"--- {course.name} ---")
        for i, assignment_weightage in enumerate(course.assignments, 1):
            grade = float(input(f"Enter grade for Assignment {i}: "))
            course.add_grade(grade)

    display_dashboard(courses)

    overall_gpa, overall_percentage = calculate_overall_grade(courses)
    print("----- Overall Grade -----")
    print(f"Overall GPA: {overall_gpa}")
    print(f"Overall Percentage: {overall_percentage}%")


if __name__ == "__main__":
    main()
