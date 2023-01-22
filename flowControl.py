# First, create a new python file in PyCharm: New>Python file. Name it "flowControl". You will now have a
# file named "flowControl.py" where you can write your code. You can also create a new file for each task(1,2 and 3).
# To run your script: right-click on the file>Run 'flowControl'
# Then, for each of the following tasks:
#
# Propose an algorithm written in pseudocode and/or a flowchart.
# Propose a solution written in python
# Task 1: Even or Odd
# 1. Write a program that determines whether a number is odd or even.
# [hint] A number is even if it can be divided by 2, and odd otherwise. In other words, the division remainder of an
# even number by 2 needs to be 0. Think of the table of arithmetic operators from the previous sessions.
oddoreven = int(input("Input a whole number: "))
if oddoreven%2 == 0:
    print("Even")
else:
    print("Odd")

# 2. Modify your program to ask the user to give a number instead. We assume that the user will enter a valid integer
# number.
#
# Task 2: Multiple of
# Write a program that takes two integer values from the user: number_1 and number_2, then says whether number_1 is a
# multiple of number_2.
#
mult1 = float(input("Enter first number: "))
mult2 = float(input("Enter number to see if first number is a multiple: "))
if mult2%mult1 == 0:
    print("The first number you entered is a multiple of the second")
else:
    print("The first number you entered is not a multiple of the second")
# Task 3: Absolute
# Write a program that gives the absolute value of a number given by the user.
# [hint] The absolute value of a given number k  is k itself if it is positive, and -k if it is negative.
posit = float(input("Enter a number: "))
if posit<0:
    print(posit*-1)
else:
    print(posit)
#
# Task 4: Grade descriptors
# 1. Create a new python file "gradeDescriptors.py".
# 2. Write a program that takes a number between 0 and 16 from the user, and displays the corresponding grade
# descriptor according to the following table:

mark = int(input("Input mark: "))
if mark == 0:
    print("Zero")
elif mark == 1:
    print("Low Fail")
elif mark == 2:
    print("Mid Fail")
elif mark == 3:
    print("Marginal Fail")
elif mark == 4:
    print("Low 3rd")
elif mark == 5:
    print("Mid 3rd")
elif mark == 6:
    print("High 3rd")
elif mark == 7:
    print("Low 2:2")
elif mark == 8:
    print("Mid 2:2")
elif mark == 9:
    print("High 2:2")
elif mark == 10:
    print("Low 2:1")
elif mark == 11:
    print("Mid 2:1")
elif mark == 12:
    print("High 2:1")
elif mark == 13:
    print("Low 1st")
elif mark == 14:
    print("Mid 1st")
elif mark == 15:
    print("High 1st")
elif mark == 16:
    print("Exceptional 1st")
else:
    print("You need to enter a number from 0-16")

#
# Mark	Grade
# 0	Zero
# 1	Low Fail
# 2	Mid Fail
# 3	Marginal Fail
# 4	Low 3rd
# 5	Mid 3rd
# 6	High 3rd
# 7	Low 2 : 2
# 8	Mid 2 : 2
# 9	High 2 : 2
# 10	Low 2 : 1
# 11	Mid 2 : 1
# 12	High 2 : 1
# 13	Low 1st
# 14	Mid 1st
# 15	High 1st
# 16	Exceptional 1st
# 3. Re-write your program to display the class only without the scale.

markshort = int(input("Input mark: "))
if markshort == 0:
    print("Zero")
elif markshort>0 and markshort<4:
    print("Fail")
elif markshort>=4 and markshort<7:
    print("3rd")
elif markshort>=7 and markshort<10:
    print("2:2")
elif markshort>=10 and markshort<13:
    print("2:1")
elif markshort>=13 and markshort<17:
    print("1st")
else:
    print("You need to enter a number from 0-16")

