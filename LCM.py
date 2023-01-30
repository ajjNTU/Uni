# 5. Least Common Multiple (LCM)
# The LCM of two divisors is the first number that both divisors can divide. For instance, the LCM of 4 and 6 is 12,
# because 12 is the first number that both 4 and 6 can divide.
#
# Create a new python file lcm.py
# Write a program that finds the LCM of two integers, given by the user.
# [hint] You can use a Boolean variable that indicates whether the LCM has been found yet. If its value is True, then
# the program should stop and print out the result.

def LCM(num1,num2):
    count = max(num1, num2)
    maxcount = num1 * num2
    if num1 == 1 or num2 == 1:
        print(maxcount)
    while count <= maxcount:
        if count%num1 == 0 and count%num2 == 0 and count > num1 and count > num2:
            print(count)
            break
        else:
            count += 1



LCM(4,6)


LCM(24,30)


LCM(2,1)

LCM(2,2)

LCM(1,2)