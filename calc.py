# calculator parts
# addition multiplication subtraction division exponents and base conversion

import math


def multi(num1, num2):
    # multiplication with addition
    total = 0
    for i in range(1, max(num2, num1) + 1):
        total += min(num1, num2)
    return print(num1, "*", num2, "=", total)


def div(numerator, denominator):
    # division to find the quotient and remainder without using "/"
    quotient = 0
    remainder = 0
    num = numerator
    dem = denominator
    posneg = 1
    if numerator < 1:
        numerator = numerator * -1
        posneg = posneg * -1
    if denominator < 1:
        denominator = denominator * -1
        posneg = posneg * -1
    while numerator >= denominator:
        numerator -= denominator
        quotient += 1
        remainder = numerator
    quotient = quotient * posneg
    remainder = remainder * posneg
    return print(num, "Divided by", dem, "Result: Quotient =", quotient, "Remainder =", remainder)


def expo(base, power):
    # exponential using recursive? haven't tested fractions or negative
    pwertotal = base
    count = 0
    while count < power - 1:
        pwertotal = pwertotal * base
        count += 1
    if power == 0:
        pwertotal = 1
    return print(base, "to the power of", power, "=", pwertotal)


def addition(addition1, addition2):
    # couldn't think of a way to replication addition without just using "+"
    # cheat way
    total = addition1 + addition2
    return print(addition1, "+", addition2, "=", total)


def subtraction(subtraction1, subtraction2):
    # same
    total = subtraction1 - subtraction2
    return print(subtraction1, "-", subtraction2, "=", total)


def rebase(input_base, digits, output_base):
    i = 0
    z = 0
    suminputbasedigits = 0
    outbasedigits = []
    # error messages
    if input_base < 2:
        raise ValueError("input base must be >= 2")
    elif sum(digits) == 0:
        return [0]
    elif output_base < 2:
        raise ValueError("output base must be >= 2")
    while z < len(digits):
        if digits[z] < 0 or digits[z] >= input_base:
            raise ValueError("all digits must satisfy 0 <= d < input base")
        else:
            z += 1
    else:
        # get the sum of the input base and digits to turn it into base 10, i think
        while i < len(digits):
            suminputbasedigits += digits[-i - 1] * input_base ** i
            i += 1
        # find what the greatest power of the output base
        jtest = int(math.log(suminputbasedigits, output_base)) + 1
        # loop these powers to get the int value from highest to lowest and removing that int to leave the remainder
        # of the sum left for next loop of lower power
        for y in reversed(range(0, jtest)):
            outbasedigits.append(int(suminputbasedigits / output_base ** y))
            suminputbasedigits -= int(suminputbasedigits / output_base ** y) * output_base ** y
        return print("Input base entered:", input_base, "# Digits entered:", digits, "# Output base required:",
                     output_base, "# Result:", outbasedigits)


# calculator interface
def calc():
    print("Welcome to my calculator")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exponents")
    print("6. Number base conversion")
    print("Enter a number 1-6 to begin calculation")

    correctinput = 0
    while correctinput == 0:
        selection = input("Enter calculation option: ")
        if int(selection) in range(1, 7):
            correctinput += 1
            selection = int(selection)
        else:
            continue
    if selection == 1:
        print("")
        print("Addition selected")
        add1 = int(input("First number to add: "))
        add2 = int(input("Second number to add: "))
        addition(add1, add2)
    elif selection == 2:
        print("")
        print("Subtratction selected")
        sub1 = int(input("First number: "))
        sub2 = int(input("Number to subtract: "))
        subtraction(sub1, sub2)
    elif selection == 3:
        print("")
        print("Multiplication selected")
        multi1 = int(input("First number to multiply: "))
        multi2 = int(input("Second number to multiply: "))
        multi(multi1, multi2)
    elif selection == 4:
        print("")
        print("Division selected")
        num = int(input("Enter numerator (top number): "))
        den = int(input("Enter denominator (bottom number: "))
        div(num, den)
    elif selection == 5:
        print("")
        print("Exponents selected")
        exp1 = int(input("Base number: "))
        exp2 = int(input("Exponent: "))
        expo(exp1, exp2)
    else:
        print("")
        print("Base conversion selected")
        ibase = int(input("Input base: "))
        dgts = input("Digits seperated by a comma (eg. 1,0,0,1,0): ")
        dgtssplit = dgts.split(",")
        digitsfinal = [int(i) for i in dgtssplit]
        obase = int(input("Output base: "))
        print(digitsfinal)
        rebase(ibase, digitsfinal, obase)


# runs calc interface and checks if user want's another calc before exiting
# looks a bit dodgy, seems to repeat itself, but it worked so i stopped
anothercalc = "Y"
while anothercalc == "Y":
    print("")
    calc()
    print("")
    anothercalc = str.lower(input("Another calc Y/N: "))
    if anothercalc == "y" or anothercalc == "yes":
        print("")
        calc()
        print("")
        anothercalc = str(input("Another calc Y/N: "))
    else:
        print("Exiting...")
        break
