print('Welcome to AskPython Quiz')
answer=input('Are you ready to play the Quiz ? (yes/no) :')
score=0
total_questions=3
 
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
 
print('Thankyou for Playing this small quiz game, you attempted',score,"questions correctly!")
mark=(score/total_questions)*100
print('Marks obtained:',mark)
print('BYE!')

