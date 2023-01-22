# Write an algorithm where the user enters student grades, assuming the class has 15 students, then calculates the class
# average and displays it on screen.

# while version
print("While loop version:")
sum = 0
count = 1
howmanygrades = int(input("How many grades to average: "))
while count <= howmanygrades:
    grade = int(input("Grade #" + str(count) + ": "))
    sum += grade
    count += 1
print("Average:", sum/howmanygrades)

#for version
print("For loop version:")
sum = 0
howmanygrades = int(input("How many grades to average: "))
for count2 in range(1, howmanygrades+1):
    grade = int(input("Grade #" + str(count2) + ": "))
    sum += grade
    count += 1
print("Average:", sum/howmanygrades)