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

    # Add Buttons for each Course
    for i in range(num_courses):
        course_button = customtkinter.CTkButton(app, text=f"Course {i+1}", font=("Arial", 15))
        course_button.pack(pady=5)

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

# Run App
app.mainloop()
