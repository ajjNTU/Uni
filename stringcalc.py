def string_calc(arithmatic):
    #   add the string calculator '1+3+5-4*10/2' in?
    #       1+3+5-20 = -11
    # BIDMAS:
    # LOOK for brackets
    #   grab brackets and do IDMAS
    #   replace brackets with IDMAS value
    #   move to next brack
    # no more brackets
    # IDMAS:
    # look for **, maybe use ^ instead so replace ** to ^? just to deal with single character
    # look for *
    # look for /
    # look for +
    # look for -
    #
    # working notes:
    # doesn't like floats so any remainder just gets 0'd. could maybe add a running total of remainders but
    #       division doesn't look at the sign of the first number
    # ignoring brackets and powers for now
    # brackets could use string calc to do calc inside bracket then string calc that? recursive like??
    #

    def counting_up():
        count_up = 0
        while arithmatic.index(char) + 2 + count_up < len(arithmatic) \
                and arithmatic[arithmatic.index(char) + 2 + count_up] not in bidmas:
            count_up += 1
        min_char = min(arithmatic.index(char) + 2 + count_up, len(arithmatic))
        counting_up_string = arithmatic[arithmatic.index(char) + 1:min_char]
        # print("up string:", counting_up_string)
        return counting_up_string

    def counting_down():
        count_down = 0
        if arithmatic.index(char) == 1:
            counting_down_string = arithmatic[0]
        else:
            while arithmatic.index(char) - 1 - count_down > 0 \
                    and arithmatic[arithmatic.index(char) - 2 - count_down] not in bidmas:
                count_down += 1
            counting_down_string = arithmatic[arithmatic.index(char) - 1 - count_down:arithmatic.index(char)]
        # print("down_string:" + counting_down_string)
        return counting_down_string

    bidmas = ['*', '/', '+', '-']
    arithmatic.replace(" ", "")
    print(f"Computing: {arithmatic}")
    while arithmatic.__contains__("*"):
        for char in arithmatic:
            if char == "*":
                up_string = counting_up()
                down_string = counting_down()
                to_replace = f"{down_string}*{up_string}"
                new_string_multi = int(int(down_string) * int(up_string))
                arithmatic = arithmatic.replace(str(to_replace), str(new_string_multi))
                # print(f"replace {to_replace} with {new_string_multi}")
                # some checks remove leading "+" or double operator
                arithmatic = arithmatic.replace("--", "+")
                arithmatic = arithmatic.replace("+-", "-")
                if arithmatic[0] == "+":
                    arithmatic = arithmatic[1:]
                # print(f"New arithmatic: {arithmatic}")
    while arithmatic.__contains__("/"):
        for char in arithmatic:
            if char == "/":
                up_string = counting_up()
                down_string = counting_down()
                to_replace = f"{down_string}/{up_string}"
                new_string_div = int(int(down_string) / int(up_string))
                arithmatic = arithmatic.replace(str(to_replace), str(new_string_div))
                # print(f"replace {to_replace} with {new_string_div}")
                # some checks remove leading "+" or double operator
                arithmatic = arithmatic.replace("--", "+")
                arithmatic = arithmatic.replace("+-", "-")
                if arithmatic[0] == "+":
                    arithmatic = arithmatic[1:]
                # print(f"New arithmatic: {arithmatic}")
    while arithmatic.__contains__("+"):
        for char in arithmatic:
            if char == "+":
                up_string = counting_up()
                down_string = counting_down()
                # look if down_string should be -
                if arithmatic[arithmatic.index(down_string) - 1] == "-":
                    down_string = "-" + down_string
                    new_string_add = int(down_string) + int(up_string)
                else:
                    new_string_add = int(down_string) + int(up_string)
                to_replace = f"{down_string}+{up_string}"
                # if down string was negative, and we end up with a positive need to replace the - with +
                if int(down_string) < 0 < int(new_string_add):
                    arithmatic = arithmatic.replace(str(to_replace), "+" + str(new_string_add))
                    # print(f"replace {to_replace} with +{new_string_add}")
                else:
                    arithmatic = arithmatic.replace(str(to_replace), str(new_string_add))
                    # print(f"replace {to_replace} with {new_string_add}")
                # some checks remove leading "+" or double operator
                arithmatic = arithmatic.replace("--", "+")
                arithmatic = arithmatic.replace("+-", "-")
                if arithmatic[0] == "+":
                    arithmatic = arithmatic[1:]
                # print(f"New arithmatic: {arithmatic}")
    final = 0
    if not arithmatic[1:].isnumeric():
        if arithmatic[0] == "-":
            subs = arithmatic[1:].split("-")
            for item in subs:
                final -= item
        else:
            subs = arithmatic.split("-")
            final += int(subs[0])
            for item in subs[1:]:
                final -= int(item)
    else:
        final = arithmatic
    print("Result:", int(final))
    return final


string_calc("4+4")
string_calc("-3*-3")
string_calc("3*-3")
string_calc("-3*3")
string_calc("3/-1+5-4*10000*-10")
string_calc("1+3+5-4*10/2")
string_calc("1-3+5-4000*10000+2*2")
string_calc("1-3+5-4000*10000+2*2*-2/-2")
string_calc("1-3+5+4000*10000-2*2*-2/2")
string_calc("1-3+5+4000*10000+2*2*2/-2")
string_calc("1-3+5-4000*10000+2*2*2/-7")
string_calc("1-3+5-4000*10000+6/-7")
string_calc("1-3+5-4000*10000+3/-7")
string_calc("1-3+5-4000*10000+3/-7+2/7")
string_calc("1-3+5+4000*10000+3/-7+2/7-17/7")

