# 4. Prime number
# Write a program that calculates all prime numbers* starting from 1 up to a value n, given by the user.
# * A Prime Number is a positive whole number, greater than 1, that has no other divisors except the number 1 and the
# number itself.
#
# If the user inputs a number below 2, print an error message.
# Print out each number that cannot be divided by any other number (that is its a prime number).
# [hint] Think of using nested loops.

def primes(max: int = 2):
    primeslist = []
    remainderlist = []
    division = 2
    if isinstance(max,int) is False:
        print("Must enter number 2 or greater")
    elif max < 2:
        print("Number must be 2 or greater")
    else:
        print("Input is", max, ":the primes equal to or less than are:")
        while max > 2:
            maxdiv = max / 2
            for division in range(2, int(maxdiv+1)+1):
                remainderlist.append(max%division)
                #print(remainderlist)
            if all(item != 0 for item in remainderlist):
                primeslist.append(max)
                #print("Added to prime list:", max)
                max -= 1
                remainderlist = []
            else:
                #print("Not added:", max)
                max -= 1
                remainderlist = []
        #print("Added to prime list: 2")
        primeslist.append(2)
        return print(primeslist)


primes(25)

primes(1)

primes(100)

primes()

primes("h")

primes(h)