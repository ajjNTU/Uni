# Task 5 [Advanced]: Quiz
# 1. Create a new python file "quiz.py".
# 2. Write a quiz program that asks the user a multiple-choice question. After the user answers the question,
# the program should display either "correct" or "incorrect".
# 3. Modify your program to include three questions instead of one.
# 4. Modify your program again to include a message at the end of the quiz that tells the user how many questions were
# answered correctly.
# [hint] you can use a variable that keeps count of correct answers. The value stored in the variable will change after
# question is answered to reflect the new count of correct answers, if any.


import datetime as dt

quizzer = input("What's your name?")
correcttotal = 0
now = dt.datetime.now()
date_of_quiz = now.strftime("%d/%m/%Y %H:%M:%S")
print("Question 1: What scale to americans use to measure temperature?")
print("A: C")
print("B: K")
print("C: F")
print("D: o")
attempt = 0
while attempt < 2:
    answer1 = input("Input answer A/B/C/D: ")
    if answer1 == "C":
        print("Correct")
        correcttotal += 1
        attempt = 2
    else:
        if attempt == 1:
            print("Incorrect")
            attempt += 1
        else:
            print("Try Again")
            attempt += 1
print("")
print("Question 2: What is Mario's brother called?")
print("A: Wario")
print("B: Luigi")
print("C: Peach")
print("D: Koopa Troopa")
attempt = 0
while attempt < 2:
    answer1 = input("Input answer A/B/C/D: ")
    if answer1 == "B":
        print("Correct")
        correcttotal += 1
        attempt = 2
    else:
        if attempt == 1:
            print("Incorrect")
            attempt += 1
        else:
            print("Try Again")
            attempt += 1
print("")
print("Question 3: What is the land of the hobbits called?")
print("A: The Shire")
print("B: Mordor")
print("C: Valynar")
print("D: Rivendale")
attempt = 0
while attempt < 2:
    answer1 = input("Input answer A/B/C/D: ")
    if answer1 == "A":
        print("Correct")
        correcttotal += 1
        attempt = 2
    else:
        if attempt == 1:
            print("Incorrect")
            attempt += 1
        else:
            print("Try Again")
            attempt += 1
print("")
print("You got", correcttotal, "/3 correct")
scores_text = open(r"C:\Users\aj104\PycharmProjects\quizScore.txt", "a", encoding="utf-8")
scores_text.write(f"\nPlayer: {quizzer} scored {correcttotal} out of 3 on {date_of_quiz}")
scores_text.close()


