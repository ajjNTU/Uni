# Session 2

# vat task from session 2
correctBD = 0
correctPRICE = 0

while correctBD == 0:
    BD = input("Is this a book or document? ")
    print(BD)
    if BD[0] == "Y" or BD[0] == "N":
        correctBD = 1
    else:
        print("Enter Y/N")
        continue
while correctPRICE == 0:
    try:
        PRICE = float(input("Purchase Price: "))
    except ValueError:
        # Not a valid number
        print("You must enter a number")
        continue
    else:
        correctPRICE = 1
if BD[0] == "Y":
    print("Price + Vat (Total):", PRICE, "+ 0 (", PRICE, ")")
elif BD[0] == "N":
    print("Price + Vat: (Total):", PRICE, "+", PRICE * .2, " (", PRICE * 1.2, ")")
else:
    print("""Answer 'Is this a book or document' question with Y/N
or use number for Purchase Price""")

# Task [1]: Perform operations between different types and check the result type each time.
# Ex: 13//2 ,  13%2 , 1-0.99, 7.5**2
print(13 / 2)
print(13 % 2)
print(1 - 0.99)
print(7.5 ** 2)
# Task [2]: Convert hours to minutes:

# Take input from the user for a given time in hours (should be in the form of 4, 2.6 etc and be between 0 and 24).
# This can be done using the input() function. Convert the value returned by the input() function from a string into
# a number using float() function. Now convert this value into minutes. This can be done by multiplying the hours by
# 60 Print out a message telling the user what is the time in minutes
htom = float(input("Enter a number: "))
print(htom * 60, "mins")
# Task [3]: Calculator for students expenses. It is the start of the academic year and students need to figure out
# how much they will be spending and if their part-time job can cover their expenses. Write a program that:

# Asks the user to enter monthly expenses (such as rent, transport, groceries, eating-out, etc ) one by one.
# Calculates the total Displays a message to indicate the calculated expenses. [hint] use input() function to collect
# expenses values, and int() or float() function to convert them from strings to numerical values.
rent = float(input("Cost of rent? "))
transport = float(input("Cost of transport? "))
groceries = float(input("Cost of groceries? "))
eatingout = float(input("Cost of eating-out? "))
utilities = float(input("Cost of utilites? "))
total = rent + transport + groceries + eatingout + utilities
print("Total expenses:", total)

# Task[1]: Consider string weather below. This is a text from BBC describing the weather in Nottingham on Friday.
# weather = "Friday\nTomorrow, variable cloud will tend to clear through the morning, with plenty of winter sunshine
# developing. However, patchy cloud and isolated showers may move in from the west later in the afternoon." 1. Split
# weather by each of the following characters: new line, space, comma, full stop. This will generate 4 different
# lists. 2. Print the length of weather. 3. Convert all the words in weather into lowercase. Save the resulting
# string in a new variable weather_lc. 4. We want to find out if there will be sunshine on Friday based on the
# description in weather. What is the best approach to do that? [hint] look for the most appropriate method in the
# table above.
weather = "Friday\nTomorrow, variable cloud will tend to clear through the morning, with plenty of winter sunshine " \
          "developing. However, patchy cloud and isolated showers may move in from the west later in the afternoon. "
print(weather.split("\n"))
print(weather.split(" "))
print(weather.split(","))
print(weather.split("."))
print(len(weather))
weather_lc = weather.lower()
print(weather_lc.find("sunshine"))
print(weather_lc.find("random"))
if weather_lc.find("sunshine") != -1:
    print("Sunshine today")
else:
    print("No sunshine today")
