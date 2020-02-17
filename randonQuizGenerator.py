##! /usr/bin/env python3
# randomQuizGenerator.py - Creates quizzes with questions and answers in
# random order, along with the answer key.

import random

# the quiz data. Keys are states and values are their capitals.Line too long ??? works for 5 only !!!
capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix','Arkansas': 'Little Rock', 'California': 'Sacramento',
            'Colorado': 'Denver',
            'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois':
            'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine':
            'Michigan':
            'Nebraska': 'Lincoln', 'Nevada':
            'New York': 'Albany', 'North Carolina': 'Raleigh',
            'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg','Rhode Island': 'Providence',
            'Tennessee':'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont':
            'Washington': 'Olympia', 'West

for quizNum in range (5):
    # todo: create the quiz and answer files
    quizFile = open('capitalsquiz%s.txt' % (quizNum +1), 'w')
    answerKeyFile = open('capitalsquiz_answers%s.txt' % (quizNum +1),'w')

    # Write out the header for the quiz.
    quizFile.write('Name:\n\nDate:\n\nPeriod:\n\n')
    quizFile.write((' ' *20) + 'State Capitals Quiz (Form %s)' %(quizNum +1))
    quizFile.write('\n\n')

    #Shuffle the order of the states.
    states = list(capitals.keys())
    random.shuffle(states)
    
    # todo: loop through all 50 states, making a question for each
    for questionNum in range(5):
        #get right and wrong anwers.
        correctAnswer = capitals[states[questionNum]]
        wrongAnswers = list(capitals.values())
        del wrongAnswers[wrongAnswers.index(correctAnswer)]
        wrongAnswers = random.sample(wrongAnswers,3)
        answerOptions = wrongAnswers + [correctAnswer]
        random.shuffle(answerOptions)

        quizFile.write('%s. What is the capital of %s?\n' % (questionNum +1,states[questionNum]))
        for i in range(4):
            quizFile.write('   %s. %s\n' %('ABCD'[i],answerOptions[i]))
        quizFile.write('\n')

        answerKeyFile.write('%s. %s\n' % (questionNum + 1, 'ABCD'[answerOptions.index(correctAnswer)]))
    quizFile.close()
    answerKeyFile.close()
    