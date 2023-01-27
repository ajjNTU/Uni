# calculator parts
# addition multiplication subtraction division exponents and base conversion
def multi(num1, num2):
    # multiplication with addition
    total = 0
    num_1_save = num1
    num_2_save = num2
    positive_or_negative = 1
    if num1 < 0:
        num1 = num1 * -1
        positive_or_negative = positive_or_negative * -1
    if num2 < 0:
        num2 = num2 * -1
        positive_or_negative = positive_or_negative * -1
    for i in range(1, max(num2, num1) + 1):
        total += min(num1, num2)
    return print(num_1_save, "*", num_2_save, "=", total * positive_or_negative)


def div(numerator, denominator):
    # division to find the quotient and remainder without using "/"
    quotient = 0
    remainder = 0
    num_input_save = numerator
    dem_input_save = denominator
    positive_or_negative = 1
    if numerator < 0:
        numerator = numerator * -1
        positive_or_negative = positive_or_negative * -1
    if denominator < 0:
        denominator = denominator * -1
        positive_or_negative = positive_or_negative * -1
    while numerator >= denominator:
        numerator -= denominator
        quotient += 1
        remainder = numerator
    quotient = quotient * positive_or_negative
    remainder = remainder * positive_or_negative
    return print(num_input_save, "Divided by", dem_input_save, "Result: Quotient =", quotient, "Remainder =", remainder)


def expo(base, power):
    # exponential using recursive?
    power_total = base
    count = 0
    while count < power - 1:
        power_total = power_total * base
        count += 1
    if power == 0:
        power_total = 1
    return print(base, "to the power of", power, "=", power_total)


def addition(addition1, addition2):
    total = addition1 + addition2
    return print(addition1, "+", addition2, "=", total)


def subtraction(subtraction1, subtraction2):
    total = subtraction1 - subtraction2
    return print(subtraction1, "-", subtraction2, "=", total)


def rebase(input_base, digits, output_base):
    exponential = 0
    digits_check_count = 0
    sum_input = 0
    output_digits = []
    # error messages
    if input_base < 2:
        raise ValueError("input base must be >= 2")
    elif sum(digits) == 0:
        return print("Input base entered:", input_base, "# Digits entered:", digits, "# Output base required:",
                     output_base, "# Result:", [0])
    elif output_base < 2:
        raise ValueError("output base must be >= 2")
    while digits_check_count < len(digits):
        if digits[digits_check_count] < 0 or digits[digits_check_count] >= input_base:
            raise ValueError("all digits must satisfy 0 <= d < input base")
        else:
            digits_check_count += 1
    else:
        # get the sum of the input base and digits to turn it into base 10, I think
        while exponential < len(digits):
            sum_input += digits[-exponential - 1] * input_base ** exponential
            exponential += 1
        # find what the greatest power of the output base
        output_base_max_exponential = 0
        max_exponential = 0
        while output_base_max_exponential <= sum_input:
            output_base_max_exponential = output_base ** max_exponential
            max_exponential += 1
        max_exponential = max_exponential - 1
        # loop these powers to get the int value from highest to lowest and removing that int to leave the remainder
        # of the sum left for next loop of lower power
        for y in reversed(range(0, max_exponential)):
            output_digits.append(int(sum_input / output_base ** y))
            sum_input -= int(sum_input / output_base ** y) * output_base ** y
        return print("Input base entered:", input_base, "# Digits entered:", digits, "# Output base required:",
                     output_base, "# Result:", output_digits)


# try and do an integer checker function
def integer_check(input_message):
    while True:
        try:
            int_check = int(input(input_message))
        except ValueError:
            print("Please use integers")
        else:
            break
    return int_check


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

    correct_input = 0
    while correct_input == 0:
        selection = input("Enter calculation option: ")
        if selection == "exit":
            correct_input = 1
        else:
            try:
                selection = int(selection)
            except ValueError:
                print("Error: Input must be a number 1-6 or 'exit'")
                print("")
            else:
                if selection in range(1,7):
                    break
                else:
                    print("Error: Input must be a number 1-6 or 'exit'")
                    print("")
    if selection == 1:
        print("")
        print("Addition selected")
        add1 = integer_check("First number to add: ")
        add2 = integer_check("Second number to add: ")
        addition(add1, add2)
    elif selection == 2:
        print("")
        print("Subtraction selected")
        sub1 = integer_check("First number: ")
        sub2 = integer_check("Number to subtract: ")
        subtraction(sub1, sub2)
    elif selection == 3:
        print("")
        print("Multiplication selected")
        multi1 = integer_check("First number to multiply: ")
        multi2 = integer_check("Second number to multiply: ")
        multi(multi1, multi2)
    elif selection == 4:
        print("")
        print("Division selected")
        num = integer_check("Enter numerator (top number): ")
        den = integer_check("Enter denominator (bottom number: ")
        div(num, den)
    elif selection == 5:
        print("")
        print("Exponents selected")
        exp1 = integer_check("Base number: ")
        exp2 = integer_check("Exponent: ")
        expo(exp1, exp2)
    elif selection == 6:
        print("")
        print("Base conversion selected")
        while True:
            try:
                in_base = int(input("Input base: "))
            except ValueError:
                print("Please use integer >= 2")
                continue
            if in_base < 2:
                print("Please use integer >= 2")
            else:
                break
        correct_digits = 0
        while correct_digits == 0:
            digits = input("Digits seperated by a comma (eg. 1,0,0,1,0): ")
            try:
                digits_split = digits.split(",")
                digits_final = [int(i) for i in digits_split]
            except ValueError:
                print("all digits must satisfy 0 <= d < input base")
                continue
            else:
                if all([0 <= x < in_base for x in digits_final]):
                    correct_digits = 1
                else:
                    print("all digits must satisfy 0 <= d < input base")
                    continue
        while True:
            try:
                out_base = int(input("Output base: "))
            except ValueError:
                print("Please use integer >= 2")
                continue
            if out_base < 2:
                print("Please use integer >= 2")
            else:
                break
        # print(digits_final)
        rebase(in_base, digits_final, out_base)
    else:
        print("")
        print("Exiting...")
    return selection


# runs calc interface and checks if user want's another calc before exiting
# to do stuff:
#   allow floats into calcs?

exit_var = 0
while exit_var == 0:
    selection_var = calc()
    if str.lower(str(selection_var)) == "exit":
        exit_var = 1
    else:
        print("")
        another_calc = str.lower(input("Another calc Y/N: "))
        if another_calc == "y" or another_calc == "yes":
            print("")
            continue
        else:
            print("")
            print("Exiting...")
            exit_var = 1



