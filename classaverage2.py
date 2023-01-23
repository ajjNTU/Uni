# 2. Class Average [Revisited]
# Re-write the program that calculates the class average as a function class_avg(grades), where grades are given as a
# list. The function should return the average (a float).
# Create a list that contains 15 values, between 0 and 16, and use it to test your function.
def class_avg(grades: list):
    total = 0
    for i in range(len(grades)):
        total += grades[i]
    print(total)
    average = total/len(grades)
    print(average)

class_avg([1,2,3,4,5])
class_avg([1,2,15,4,5])
class_avg([1,2,100,4,20,0])
# Re-write your NTU undergraduate grading scale convertor program from last week as a function grading_scale(grade).
# Use it to convert the obtained class average.
# Example:
# grading_scale(9.2) should return "High 2:2"
# grading_scale(13.5) and grading_scale(12.6) should both return "Low 1st".
def grade(marks):
    correctvalue = 0
    while correctvalue == 0:
        try:
            mark = marks
            # mark = float(input("Input a mark (0-16)\n\t>>>>>>>: "))
        except ValueError:
            print("Has to be a number from 0 to 16")
            continue
        else:
            if mark<0 or mark>16:
                print("Has to be a number from 0 to 16")
                continue
            else:
                correctvalue = 1
                if mark - int(mark) < .5:
                    mark = int(mark)
                else:
                    mark = int(mark)+1


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


grade(9.2)
grade(9.7)
grade(9)



# Extend your program to take grades from the user instead and store them in a list. We assume that we do not know the
# number of students beforehand.
#????
#????
#????
#????


# Re-write function class_avg(grades) so that grades are given in a dictionary where the key is the student ID and the
# value is the student grade.

def class_avg_dict(grades: dict):
    total = 0
    for i in range(len(grades)):
        print(grades['grade'])
        total += grades['grade']

class_avg_dict({'key': 1, 2 'grade': 12, 14})


