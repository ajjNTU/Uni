# 2. Quiz [Revisited]
# We want to extend the quiz to program so that: 1) Your quiz questions are saved in a file. 2) Scores are saved to a
# file at the end of each round.
#
# You will need to open the file in write mode.
# Extend your previous quiz program so that it asks for the player's name, then saves the score (correct answers) of
# each player in a file "quizScores.txt"
# It can be in the form
# Player: Joy ; Score: 3
# Extend your program to save the timestamp when the scores are saved. [hint] You can use the datetime module.
# Do you see any redundant code in your program? If yes, propose a solution to improve it.
# [Challenge] Extend your program so that it simultaneously reads questions and corresponding answers from quiz.txt ,
# displays the questions to the user and saves the score to quizScores.txt .
quiz = open(r"C:\Users\aj104\PycharmProjects\quiz.txt", "w", encoding="utf-8")
#quiz.truncate()
quiz.write("Question 1\nMario's brother is called...\nWario\nPeach\nLuigi\nKoopa\ncorrect:Wario\n\n"
           "Question 2\nThe hobbits live in...\nThe Shire\nMordor\nValynar\nRivendale\ncorrect:The Shire\n\n"
           "Question 3\nAmericans use what temperate scale?\nC\nK\nF\nN\ncorrect:F\n\n"
           "Question 4\nHow do you open a utf-8 encoded text file in phython for reading?\nopen(filepath, 'w', "
           "encoding='utf-8')\nopen(fiilepath, 'r', encoding='utf-8')\nopen(nothing, 'what am i doing', "
           "encoding='dunno')\nopen(fiilepath, encoding='utf-8')\ncorrect: open(fiilepath, encoding='utf-8')")
quiz.close()

# my complicated idea:
# open quiz, ask name input,split questions up, grab correct variable, print question, inputs for answers,
# counter for correct + 2 attempts, next question, end of questions show total correct
# and write to a file saving scores, name and timestamp
#
# what is asked for just add the scores file to my old quiz
"""
see quiz.py for this
"""
