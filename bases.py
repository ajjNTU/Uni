import math


def rebase(input_base, digits, output_base):
    i = 0
    j = 0
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


rebase(97, [3, 46, 60], 73)
rebase(16, [2, 10], 3)
rebase(10, [4, 2], 2)
rebase(10, [3,2,4,7,5], 2)
rebase(2, [1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1], 10)