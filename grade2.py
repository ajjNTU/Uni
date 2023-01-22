# Task 4: Grade descriptors
# 1. Create a new python file "gradeDescriptors.py".
# 2. Write a program that takes a number between 0 and 16 from the user, and displays the corresponding grade
# descriptor according to the following table:


correctvalue = 0
while correctvalue == 0:
    try:
        mark = int(input("Input a mark (0-16)\n\t>>>>>>>: "))
    except ValueError:
        print("Has to be a whole number from 0 to 16")
        continue
    else:
        if mark<0 or mark>16:
            print("Has to be a whole number from 0 to 16")
            continue
        else:
            correctvalue = 1
if mark%3 == 1:
    scale = "Low"
elif mark%3 == 2:
    scale = "Mid"
elif mark%3 == 0:
    scale = "High"
if mark/15 <= .2:
    classn = "Fail"
elif mark/15 <= .4:
    classn = "3rd"
elif mark/15 <= .6:
    classn = "2:2"
elif mark/15 <= .8:
    classn = "2:1"
elif mark/15 <= 1:
    classn = "1st"
if mark == 16:
    scale = "Exceptional"
    classn = "1st"
elif mark == 3:
    scale = "Marginal"
if mark == 0:
    print("Result:")
    print("Class is Zero")
    print("Zero")
else:
    print("Result:")
    print("Scale is", scale, "# Class is", classn)
    print(scale, classn)