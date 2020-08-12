#asks user to solve muliplication tasks, after 3 wrong inputs we go to next question, after 8 seconds evey answer is timeout wrong

import pyinputplus as pyip, time, random

for i in range(10): #10 questions 
    try:
        firstNumber = random.randint(0,9) #random number between 0-9 and 0-9 (13-22-55etc.)
        secondNumber = random.randint(0,9)
        wrongCount = 0
        while wrongCount <3: #user get 3 tries to answer correct, after that we go to next question
            if pyip.inputInt(f"{firstNumber} * {secondNumber} = ",timeout=8) == firstNumber*secondNumber: #after 8 seconds the question is marked incorrect, even if the given answer after 8 seconds is correct
                print("Correct") #if answer is corrct, promp "Correct" for one second
                wrongCount = 0
                time.sleep(1)
                break
            else:
                wrongCount +=1
    except:
        print("You have to answer in 8 seconds")