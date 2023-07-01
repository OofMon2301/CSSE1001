import tkinter
import customtkinter

# Our App Frame
app = customtkinter.CTk()
app.geometry("1280x720")
app.title("Uni Calculator")
app.resizable(True, True)

# Read the previously saved value
try:
    with open("course_info.txt", "r") as file:
        num_courses = int(file.read())
except FileNotFoundError:
    num_courses = 0


def enter_button_clicked():
    global num_courses
    num_courses = int(link.get())

    # Save the updated value to a file
    with open("course_info.txt", "w") as file:
        file.write(str(num_courses))

    # Destroy Previous Page
    title.pack_forget()
    link.pack_forget()
    enter_button.pack_forget()

    # Create Entry Fields and Labels for each Course
    for i in range(num_courses):
        course_label = customtkinter.CTkLabel(app, text=f"Course {i+1}:", font=("Arial", 15))
        course_label.pack(pady=5)
        course_labels.append(course_label)

        course_entry = customtkinter.CTkEntry(app, width=450, height=40, font=("Arial", 15))
        course_entry.insert(0, f"Course {i+1}")  # Pre-fill the entry with course name
        course_entry.pack()
        course_entries.append(course_entry)

    # Save Button
    save_button = customtkinter.CTkButton(app, text="Save", command=save_courses, font=("Arial", 20), width=15, height=2)
    save_button.pack(pady=20)

def save_courses():
    course_names = [entry.get() for entry in course_entries]

    # Save the course names to a file
    with open("course_names.txt", "w") as file:
        for course_name in course_names:
            file.write(course_name + "\n")

    # Destroy Previous Page
    for label in course_labels:
        label.pack_forget()
    for entry in course_entries:
        entry.pack_forget()

    # Create Overview with Course Buttons
    for i, course_name in enumerate(course_names):
        course_button = customtkinter.CTkButton(app, text=course_name, font=("Arial", 15), width=20, height=2)
        course_button.pack(side="left", padx=10, pady=10)

        add_assignment_button = customtkinter.CTkButton(app, text="Add Assignment", font=("Arial", 12), width=15)
        add_assignment_button.pack(side="left", padx=10, pady=10)

def load_courses():
    # Read the previously saved course names
    try:
        with open("course_names.txt", "r") as file:
            course_names = file.readlines()
        course_names = [name.strip() for name in course_names]
    except FileNotFoundError:
        course_names = []

    # Create Overview with Course Buttons
    for i, course_name in enumerate(course_names):
        course_button = customtkinter.CTkButton(app, text=course_name, font=("Arial", 15), width=20, height=2)
        course_button.pack(side="left", padx=10, pady=10)

        add_assignment_button = customtkinter.CTkButton(app, text="Add Assignment", font=("Arial", 12), width=15)
        add_assignment_button.pack(side="left", padx=10, pady=10)

# Update the UI for enter_button
enter_button = customtkinter.CTkButton(app, text="Enter", command=enter_button_clicked, font=("Arial", 15))

# Pack the UI Elements into the App and ask user to type amount of assignments for each course, counting individually
title = customtkinter.CTkLabel(app, text="Please Type the Amount of Courses you currently study:", font=("Arial", 15))
title.pack(padx=10, pady=10)

# Inputs
url_var = tkinter.StringVar()
link = customtkinter.CTkEntry(app, width=450, height=40, textvariable=url_var, font=("Arial", 15))
link.insert(0, str(num_courses))  # Pre-fill the input field with the loaded value
link.pack()

# Enter Button
enter_button = customtkinter.CTkButton(app, text="Enter", command=enter_button_clicked, font=("Arial", 15))
enter_button.pack(padx=10, pady=15)

# System Settings
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

# Load the saved course information
load_courses()

# Run App
app.mainloop()
