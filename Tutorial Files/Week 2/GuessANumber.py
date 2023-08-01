import random

num1 = random.randint(1, 100)
print("Try to guess the number I am thinking of between 1 and 100.")
number = int(input("Please enter your guess: "))
if number == int(-1):
    print("The number you were trying to guess was " + str(num1) + ".")
    exit(1)
if number != num1:
    while number != num1:
        print("Sorry that is not correct.")
        number = int(input("Please enter your guess: "))
        if number == int(-1):
            print("The number you were trying to guess was " + str(num1) + ".")
            exit(1)
        if number == num1:
            print("Congratulations! You guessed the number correctly!")
            break


print("Congratulations! You guessed the number correctly!")
