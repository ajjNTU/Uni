def string_calc(arithmatic):
    #   add the string calculator '1+3+5-4*10/2' in?
    #       1+3+5-20 = -11
    # BIDMAS
    # LOOK for brackets
    #   grab brackets and do IDMAS
    #   replace brackets with IDMAS value
    #   move to next brack
    # no more brackets
    # look for ** and replace ** with value
    # look for *
    # look for +
    # look for -
    #
    # working notes:
    # ignoring brackets and powers for now

    def counting_up():
        count_up = 0
        while arithmatic.index(char) + 2 + count_up < len(arithmatic) and arithmatic[
            arithmatic.index(char) + 2 + count_up] not in bidmas:
            count_up += 1
        minchar = min(arithmatic.index(char) + 2 + count_up, len(arithmatic))
        up_string = arithmatic[arithmatic.index(char) + 1:minchar]
        #print("up string:", up_string)
        return up_string

    def counting_down():
        count_down = 0
        if arithmatic.index(char) == 1:
            down_string = arithmatic[0]
        else:
            while arithmatic[arithmatic.index(char) - 2 - count_down] not in bidmas:
                count_down += 1
            down_string = arithmatic[arithmatic.index(char) - 1 - count_down:arithmatic.index(char)]
        #print("down_string:" + down_string)
        return down_string

    bidmas = ['*', '/', '+', '-']
    #arithmatic.replace(" ", "")
    print(arithmatic)
    while arithmatic.__contains__("*"):
        for char in arithmatic:
            if char == "*":
                up_string = counting_up()
                down_string = counting_down()
                to_replace = f"{down_string}*{up_string}"
                new_string_multi = int(int(down_string) * int(up_string))
                arithmatic = arithmatic.replace(str(to_replace), str(new_string_multi))
                #print(f"replace {to_replace} with {new_string_multi}")
                # some checks remove leading "+" or double operator
                arithmatic = arithmatic.replace("--", "+")
                arithmatic = arithmatic.replace("+-", "-")
                if arithmatic[0] == "+":
                    arithmatic = arithmatic[1:]
                #print(f"New arithmatic: {arithmatic}")
    while arithmatic.__contains__("/"):
        for char in arithmatic:
            if char == "/":
                up_string = counting_up()
                down_string = counting_down()
                to_replace = f"{down_string}/{up_string}"
                new_string_div = int(int(down_string) / int(up_string))
                arithmatic = arithmatic.replace(str(to_replace), str(new_string_div))
                #print(f"replace {to_replace} with {new_string_div}")
                # some checks remove leading "+" or double operator
                arithmatic = arithmatic.replace("--", "+")
                arithmatic = arithmatic.replace("+-", "-")
                if arithmatic[0] == "+":
                    arithmatic = arithmatic[1:]
                #print(f"New arithmatic: {arithmatic}")
    while arithmatic.__contains__("+"):
        for char in arithmatic:
            if char == "+":
                up_string = counting_up()
                down_string = counting_down()
                # look if down_string should be - and make it *-1 if so
                if arithmatic[arithmatic.index(down_string) - 1] == "-":
                    down_string = "-" + down_string
                    new_string_add = int(down_string) + int(up_string)
                else:
                    new_string_add = int(down_string) + int(up_string)
                to_replace = f"{down_string}+{up_string}"
                # if down string was negative, and we end up with a positive need to replace the - with +
                if int(down_string) < 0 < int(new_string_add):
                    arithmatic = arithmatic.replace(str(to_replace), "+" + str(new_string_add))
                    #print(f"replace {to_replace} with +{new_string_add}")
                else:
                    arithmatic = arithmatic.replace(str(to_replace), str(new_string_add))
                    #print(f"replace {to_replace} with {new_string_add}")
                # some checks remove leading "+" or double operator
                arithmatic = arithmatic.replace("--", "+")
                arithmatic = arithmatic.replace("+-", "-")
                if arithmatic[0] == "+":
                    arithmatic = arithmatic[1:]
                #print(f"New arithmatic: {arithmatic}")
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
    print("final:", int(final))
    return final


string_calc("4+4")
string_calc("-3*-3")
string_calc("3*-3")
string_calc("3/-1+5-4*10000*-10")
string_calc("1+3+5-4*10/2")
string_calc("1-3+5-4000*10000+2*2")
string_calc("1-3+5-4000*10000+2*2*-2/-2")
string_calc("1-3+5-4000*10000+2*2*-2/2")
string_calc("1-3+5-4000*10000+2*2*2/-2")