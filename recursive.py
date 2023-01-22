# 1. Write in python a recursive function sum_up_to(n) that calculates the sum of all natural numbers from 1 up to a
# given number n.
# 2. Write a recursive function is_prime(n) that determines if a given number n is a prime number* or not.
# * A prime number is a whole number greater than 1 that cannot be divided by any whole number other than itself and 1
# (e.g. 2, 3, 5, 7, 11).
def sum_up_to(num):
    total = 0
    if num < 2:
        print("Number should be 1 or greater")
    else:
        for i in range(num+1):
            total += i
        print("Total of all numbers up to and including", num, "Total is:", total)


def is_prime(num):
    remainderlist = []
    for i in range(2, num):
        remainderlist.append(num%i)
    print(num)
    # print(remainderlist)
    if all(remainderlist) != 0:
        print("Prime")
    else:
        print("Not Prime")


sum_up_to(4)
sum_up_to(6)
sum_up_to(-5)
sum_up_to(10000)

is_prime(2)
is_prime(7)
is_prime(4)
is_prime(12)
is_prime(13)
is_prime(21)
is_prime(23)