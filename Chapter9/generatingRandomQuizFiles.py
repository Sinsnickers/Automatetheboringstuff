#! python3
#randomQuizGenerator.py - creates random quizzes with answers in
#random order along with the answer key

import random
#The quiz data -  keys are states and values their capital
capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
   'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
   'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
   'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois':
   'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas':
   'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine':
   'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan':
   'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri':
   'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada':
   'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 
   'New Mexico': 'Santa Fe', 'New York': 'Albany',
   'North Carolina': 'Raleigh', 'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
   'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
   'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee':
   'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont':
   'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 
   'West Virginia': 'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}

   #Generate 35 quiz files
for quizNum in range(35):
    # TODO: Create the quiz and answer key files.
   quizFile = open(f"capitalsquiz{quizNum+1}.txt","w")
   answerKeyFile = open(f"capitalsquiz_answers{quizNum+1}.txt","w")
    # TODO: Write out the header for the quiz.
   quizFile.write("Name:\n\nDate:\n\nPeriod:\n\n")
   quizFile.write((" "*20)+f"State Capitals Quiz(Form {quizNum+1})")
   quizFile.write("\n\n")
    # TODO: Shuffle the order of the states.
   states = list(capitals.keys())
   random.shuffle(states)

    # TODO: Loop through all 50 states, making a question for each.
    #Get rid of the wrong answers
   for questionNum in range(50):
      correctanswer = capitals[states[questionNum]]
      wronganswers = list(capitals.values())
      del wronganswers [wronganswers.index(correctanswer)]
      wronganswers = random.sample(wronganswers,3)
      answerOptions = wronganswers + [correctanswer]
      random.shuffle(answerOptions)
   
    #write the questions and answer options to the file
      quizFile.write(f"{questionNum+1}. What is the capital of {states[questionNum]}?\n\n")
      for i in range(4):
         quizFile.write(f"{'ABCD'[i]}.{answerOptions[i]}\n")
         quizFile.write('\n')

    # Write the answer key to a file.
      answerKeyFile.write(f"{questionNum + 1}.{'ABCD'[answerOptions.index(correctanswer)]}\n")
quizFile.close()
answerKeyFile.close()