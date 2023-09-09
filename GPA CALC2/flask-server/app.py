from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# Our App Frame
@app.route('/')
def index():
    # Read the previously saved value
    try:
        with open("course_info.txt", "r") as file:
            num_courses = int(file.read())
    except FileNotFoundError:
        num_courses = 0

    return render_template("index.html", num_courses=num_courses)

@app.route('/enter', methods=['POST'])
def enter():
    num_courses = int(request.form['num_courses'])

    # Save the updated value to a file
    with open("course_info.txt", "w") as file:
        file.write(str(num_courses))

    return redirect('/course')

@app.route('/course')
def course():
    # Read the previously saved course names
    try:
        with open("course_names.txt", "r") as file:
            course_names = file.readlines()
        course_names = [name.strip() for name in course_names]
    except FileNotFoundError:
        course_names = []

    return render_template("course.html", course_names=course_names)

@app.route('/overview', methods=['POST', 'GET'])
def overview():
    if request.method == 'POST':
        course_names = request.form.getlist('course_name')

        # Save the course names to a file
        with open("course_names.txt", "w") as file:
            for course_name in course_names:
                file.write(course_name + "\n")

        return redirect('/overview')
    else:
        # Read the saved course names
        try:
            with open("course_names.txt", "r") as file:
                course_names = file.readlines()
            course_names = [name.strip() for name in course_names]
        except FileNotFoundError:
            course_names = []

        unique_course_names = list(set(course_names))  # Remove duplicates

        return render_template("overview.html", unique_course_names=unique_course_names)


if __name__ == '__main__':
    app.run(debug=True)
