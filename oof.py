print('Welcome to AskPython Quiz')
answer=input('Are you ready to play the Quiz ? (yes/no) :')
score=0
total_questions=7
 
if answer.lower()=='yes':
    answer=input('Question 1: What is your Favourite programming language?')
    if answer.lower()=='python':
        score += 1
        print('correct')
    else:
        print('Wrong Answer :(')
 
 
    answer=input('Question 2: Do you follow any author on AskPython? ')
    if answer.lower()=='yes':
        score += 1
        print('correct')
    else:
        print('Wrong Answer :(')
 
    answer=input('Question 3: What is the name of your favourite website for learning Python?')
    if answer.lower()=='askpython':
        score += 1
        print('correct')
    else:
        print('Wrong Answer :(')

    answer=input('Question 4: What is your favourite game?')
    if answer.lower()=='valorant':
        score += 1
        print('correct')
    else:
        print('Wrong Answer :(')

    answer=input('Question 5: What is your favourite food?')
    if answer.lower()=='pizza':
        score += 1
        print('correct')
    else:
        print('Wrong Answer :(')

    answer=input('Question 6: What is your favourite drink?')
    if answer.lower()=='coke':
        score += 1
        print('correct')
    else:
        print('Wrong Answer :(')

# Question number 7 for the quiz is to make a very very difficult maths question that will require the user to have university level math knowledge.
    answer=input('Question 7: Suppose you have experimental data of the type (x, y), and you want to find a relationship between the variables x and y. This relationship may sometimes be determined by finding a polynomial which passes through all the points. Suppose that A(1, 6), B(2, 3) and C(3, 2) are points on a parabola y = ax^2 + bx + c. Set up a system of equations in a, b and c. Write the system of equations in matrix form. Use matrices to solve the system of equations.')
    if answer.lower()=='x^2-6x+1':
        score += 1
        print('correct')
    else:
        print('Wrong Answer :( - You suck at maths')
# Indeterminate amount of time to pause before thanking the user for playing the quiz.
    import time
    time.sleep(5)

print('Thankyou for Playing this small quiz game, you attempted',score,"questions correctly!")
mark=(score/total_questions)*100
print('Marks obtained:',mark)
print('BYE!')
# print ascii art of lenny face
print("  ( ͡° ͜ʖ ͡°)")


