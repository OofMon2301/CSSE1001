import random

# Title

print("Welcome to Alice's Addition Academy! Try out these questions below!")
correct = 0

# Asking how many questions

print("How many questions do you want to attempt?")
int_questions = int(input())
questions = int_questions

# Asking questions

while int_questions > 0:
    int1 = random.randint(10, 99)
    int2 = random.randint(10, 99)
    print("What is " + str(int1) + " + " + str(int2) + "?")
    int_answer = int(input())
    if int_answer == int1 + int2:
        print("Correct!")
        correct = correct + 1
    else:
        print("Incorrect!")
    int_questions = int_questions - 1

# Print (This is extra)
print("Thanks for playing!")
print("You got " + str(correct) + " out of " + str(questions) + " correct!")
