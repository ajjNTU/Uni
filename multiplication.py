def multi(num1, num2):
    total = 0
    for i in range(1,num2+1):
        total += num1
    return print(total)


def div(numerator, denominator):
    quotient = 0
    remainder = 0
    while numerator >= denominator:
        numerator -= denominator
        quotient += 1
        remainder = numerator
    return print(quotient, " ", remainder)


def expo(base, power):
    pwertotal = base
    count = 0
    while count < power-1:
        pwertotal = pwertotal * base
        count += 1
    if power == 0:
        pwertotal = 1
    return print(pwertotal)



multi(5,3)

multi(15,25)

div(4,2)

div(10,2)

div(15,5)

div(13,5)

div(1001,33)

expo(2,2)

expo(3,3)

expo(15,2)

expo(4,4)

expo(2,15)

expo(15,1)

expo(30,1)

expo(1,1)

expo(1,0)

expo(15,0)