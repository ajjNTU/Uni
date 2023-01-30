# Activity: Exceptions
# In our previous exercises there were several cases where exceptions could occur.  We have even used if-statements to
# avoid some of them. In this session, we are going to revisit these exercises.
#
# Remember to commit changes using git to keep track of your updates.
#
# 1. Perimeter of a rectangle
# Write in python a function that calculates the perimeter of a rectangle. This function should raise value error
# exceptions if the given width and height are not positive integers.
def p_of_t(x, y):
    try:
        x = int(x) * 2
        y = int(y) * 2
        perimeter = x + y
    except ValueError:
        print("Please enter a positive integer >0")
    else:
        if x <= 0:
            print("Please enter a positive integer >0")
        if y <= 0:
            print("Please enter a positive integer >0")
    return perimeter


# p_of_t(0, 1)
# p_of_t(2, -1)


def p_of_t_raise(x: int, y: int):
    if x <= 0 or y <= 0:
        raise ValueError(f"Either {x} or {y} are 0 or negative. Please use positive integers")
    per = 2 * x + 2 * y
    return print("Perimeter is %d" % per)


p_of_t_raise(2, 2)


# p_of_t_raise(0,2)
#
# 2. Square root
# Write in python function calc_sqrt (k) which calculates the square root of a given number k, raising a value error if
# k is negative. This requires function sqrt from the math module.
def square_root(a: int):
    import math

    if a <= 0:
        raise ValueError("%a is negative or 0" % a)
    sr = math.sqrt(a)
    print(sr)
    return sr


# square_root(-1)
# square_root(0)
# square_root(2)
# square_root(4)
# square_root(16)

# 3. Divide by many
# Write in python function div\_by_many (p, qs) which returns a list with all divisions of p by the elements of given
# list qs. The function should return the empty list if a ZeroDivisionError is raised.
def div_by_many(p: int, qs: list):
    div = []
    for q in qs:
        if q == 0:
            div = []
            break
        div.append(p / q)
    print(div)
    return div


div_by_many(150, [1, 2, 15, 25, 50, 75, 74])
div_by_many(100, [1, 2, 4, 25, 0])


#
# 3. Least Common Multiple [Revisited]
# In the previous session, you wrote a function that finds the least common multiple of two values.
#
# Try the following example: print(lcm(6,0)). What output do you get?
# Add a try/except block to handle this exception. Include a message to the user that the value given is invalid.
def LCM(num1, num2):
    """
    this is a mess atm need to work on it
    LCM%num1 == 0, LCM%num2 == 0, num1 > 0, num2 > 0
    something like this? default num1, num2 == 2?
    :param num1: first number of to find lcm from
    :param num2: second number to find the lcm from
    :return: should return the lowest common multiple
    """
    pass


print(LCM(24, 15))
print(LCM(6, 0))
print(LCM(0, 6))
# 3. Class Average, Binary Conversion, Prime Number [Revisited]
# In these exercises, we have functions where only positive values should be accepted.

#
# Extend both of your programs to raise a ValueError exception if a the value given is negative.
# 4. Calculator [Revisited]
# In this exercise, you collect input from user. If the user enters a character, an error will occur and your program
# will stop.
# ValueError: invalid literal for int() with base 10: <char>
# We want to prevent this by implementing error handling.
"""
See calc.py I haven't followed this exactly
"""
#
# Wrap the user input in your program in a try/except block. Print a message to the user that indicates the error that
# has occurred.
# 5. File Handling [Revisited]
# In the previous session, you worked with different files such as prideandprejudice.txt and quiz.txt. You might have
# noticed that if you give the wrong file name or path you get an error "FileNotFoundError".
#
# Add a try/except block to handle these exceptions.
"""
add in try except block for path and filename open and let them re-enter it if no file found?
todo: this ^^
"""
