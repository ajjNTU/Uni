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


