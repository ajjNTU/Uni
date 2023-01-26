# calculator parts
# addition multiplication subtraction division exponents and base conversion
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
        return print("Input base entered:", input_base, "# Digits entered:", digits, "# Output base required:",
                     output_base, "# Result:", [0])
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
        jtest = 0
        count = 0
        while jtest <= suminputbasedigits:
            jtest = output_base ** count
            count += 1
        count = count - 1
        # loop these powers to get the int value from highest to lowest and removing that int to leave the remainder
        # of the sum left for next loop of lower power
        for y in reversed(range(0, count)):
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
    print("Enter a number 1-6 to begin calculation or 'exit' to stop")
    print("")

    correctinput = 0
    while correctinput == 0:
        selection = input("Enter calculation option: ")
        if selection == "exit":
            correctinput = 1
        else:
            try:
                if int(selection) in range(1, 7):
                    correctinput = 1
                    selection = int(selection)
            except ValueError:
                print("Error: Input must be a number 1-6 or 'exit'")
                print("")
            else:
                print("Error: Input must be a number 1-6 or 'exit'")
                print("")
    if selection == 1:
        print("")
        print("Addition selected")
        while True:
            try:
                add1 = int(input("First number to add: "))
            except ValueError:
                print("Please use integers")
            else:
                break
        while True:
            try:
                add2 = int(input("Second number to add: "))
            except ValueError:
                print("Please use integers")
            else:
                break
        addition(add1, add2)
    elif selection == 2:
        print("")
        print("Subtratction selected")
        while True:
            try:
                sub1 = int(input("First number: "))
            except ValueError:
                print("Please use integers")
            else:
                break
        while True:
            try:
                sub2 = int(input("Number to subtract: "))
            except ValueError:
                print("Please use integers")
            else:
                break
        subtraction(sub1, sub2)
    elif selection == 3:
        print("")
        print("Multiplication selected")
        while True:
            try:
                multi1 = int(input("First number to multiply: "))
            except ValueError:
                print("Please use integers")
            else:
                break
        while True:
            try:
                multi2 = int(input("Second number to multiply: "))
            except ValueError:
                print("Please use integers")
            else:
                break
        multi(multi1, multi2)
    elif selection == 4:
        print("")
        print("Division selected")
        while True:
            try:
                num = int(input("Enter numerator (top number): "))
            except ValueError:
                print("Please use integers")
            else:
                break
        while True:
            try:
                den = int(input("Enter denominator (bottom number: "))
            except ValueError:
                print("Please use integers")
            else:
                break
        div(num, den)
    elif selection == 5:
        print("")
        print("Exponents selected")
        while True:
            try:
                exp1 = int(input("Base number: "))
            except ValueError:
                print("Please use integers")
            else:
                break
        while True:
            try:
                exp2 = int(input("Exponent: "))
            except ValueError:
                print("Please use integers")
            else:
                break
        expo(exp1, exp2)
    elif selection == 6:
        print("")
        print("Base conversion selected")
        while True:
            try:
                ibase = int(input("Input base: "))
            except ValueError:
                print("Please use integer >= 2")
                continue
            if ibase < 2:
                print("Please use integer >= 2")
            else:
                break
        correctdigits = 0
        while correctdigits == 0:
            dgts = input("Digits seperated by a comma (eg. 1,0,0,1,0): ")
            try:
                dgtssplit = dgts.split(",")
                digitsfinal = [int(i) for i in dgtssplit]
            except ValueError:
                print("all digits must satisfy 0 <= d < input base")
                continue
            else:
                if all([0 <= x < ibase for x in digitsfinal]):
                    correctdigits = 1
                else:
                    print("all digits must satisfy 0 <= d < input base")
                    continue
        while True:
            try:
                obase = int(input("Output base: "))
            except ValueError:
                print("Please use integer >= 2")
                continue
            if obase < 2:
                print("Please use integer >= 2")
            else:
                break
        # print(digitsfinal)
        rebase(ibase, digitsfinal, obase)
    else:
        print("")
        print("Exiting...")
    return selection


# runs calc interface and checks if user want's another calc before exiting
# to do stuff:
#   allow floats into calcs?
#   maybe define a function that checks input for type to call instead of all the above try excepts?
#

exitvar = 0
while exitvar == 0:
    selectionvar = calc()
    if str.lower(str(selectionvar)) == "exit":
        exitvar = 1
    else:
        print("")
        anothercalc = str.lower(input("Another calc Y/N: "))
        if anothercalc == "y" or anothercalc == "yes":
            print("")
            continue
        else:
            print("")
            print("Exiting...")
            exitvar = 1
