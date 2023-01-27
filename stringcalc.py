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
    BIDMAS = ['*', '/', '+', '-']
    print(arithmatic)
    pos_neg = 1
    for char in arithmatic:
        if char == "*":
            count_up = 0
            while arithmatic.index(char)+2+count_up < len(arithmatic) and arithmatic[arithmatic.index(char)+2+count_up] not in BIDMAS:
                count_up += 1
            minchar = min(arithmatic.index(char)+2+count_up, len(arithmatic))
            multi1 = arithmatic[arithmatic.index(char)+1:minchar]
            print("multi1", multi1)
            count_down = 0
            if arithmatic.index(char) == 1:
                multi2 = arithmatic[0]
                #print(multi2)
            else:
                while arithmatic[arithmatic.index(char)-2-count_down] not in BIDMAS:
                    count_down += 1
                multi2 = arithmatic[arithmatic.index(char) - 1 - count_down:arithmatic.index(char)]
            print("multi2", multi2)
            replacement = arithmatic[arithmatic.index(multi2):minchar]
            print("replace", replacement)
            arithmatic = arithmatic.replace(str(replacement), str(int(multi1) * int(multi2)))
            print("with", str(int(multi1) * int(multi2)))
            print(arithmatic)
            arithmatic = arithmatic.replace("--", "+")
            arithmatic = arithmatic.replace("+-", "-")
            print("replace -- to + and +- to -", arithmatic)
            if arithmatic[0] == "+":
                arithmatic = arithmatic[1:]
            print(arithmatic)
    for char in arithmatic:
        if char == "/":
            count_up = 0
            while arithmatic.index(char)+2+count_up < len(arithmatic) and arithmatic[arithmatic.index(char)+2+count_up] not in BIDMAS:
                count_up += 1
            minchar = min(arithmatic.index(char)+2+count_up, len(arithmatic))
            div1 = arithmatic[arithmatic.index(char)+1:minchar]
            print(div1)
            count_down = 0
            if arithmatic.index(char) == 1:
                div2 = arithmatic[0]
                print(div2)
            else:
                while arithmatic[arithmatic.index(char)-2-count_down] not in BIDMAS:
                    count_down += 1
                div2 = arithmatic[arithmatic.index(char)-1-count_down:arithmatic.index(char)]
            print(div2)
            replacement = arithmatic[arithmatic.index(char)-1-count_down:minchar]
            print(replacement)
            arithmatic = arithmatic.replace(str(replacement), str(int(int(div2) / int(div1))))
            print(arithmatic)
    for char in arithmatic:
        #print("working on ", char, "index", arithmatic.index(char))
        if char == "+":
            print("char is", char, "index is", arithmatic.index(char))
            count_up = 0
            while arithmatic.index(char)+2+count_up < len(arithmatic) and arithmatic[arithmatic.index(char)+2+count_up] not in BIDMAS:
                count_up += 1
            minchar = min(arithmatic.index(char)+2+count_up, len(arithmatic))
            add1 = arithmatic[arithmatic.index(char)+1:minchar]
            print(add1)
            count_down = 0
            if arithmatic.index(char) == 1:
                add2 = arithmatic[0]
            else:
                while arithmatic.index(char)-2-count_down < 0 and arithmatic[arithmatic.index(char)-2-count_down] not in BIDMAS:
                    count_down += 1
                if arithmatic[arithmatic.index(char)-2-count_down] == "-":
                    add2 = arithmatic[arithmatic.index(char) - 2 - count_down:arithmatic.index(char)]
                else:
                    add2 = arithmatic[arithmatic.index(char)-1-count_down:arithmatic.index(char)]
            print(add2)
            if add2[0] == "+":
                replacement = arithmatic[arithmatic.index(char)-1:minchar]
            print(arithmatic)
            #print("replacement is", replacement)
            #print("with", str(int(int(add2) + int(add1))))
            if arithmatic.index(char) > 2:
                replacement = arithmatic[arithmatic.index(add2):minchar]
                arithmatic = arithmatic.replace(str(replacement), "+" + str(int(int(add2) + int(add1))))
                print("replacement is", replacement)
                print("with", "+" + str(int(int(add2) + int(add1))))
            else:
                replacement = arithmatic[arithmatic.index(add2):minchar]
                arithmatic = arithmatic.replace(str(replacement), str(int(int(add2) + int(add1))))
                print("else replace is", replacement)
                print("with", str(int(int(add2) + int(add1))))
            print(arithmatic)
            arithmatic = arithmatic.replace("++","+")
            print(arithmatic)
    for char in arithmatic[1:]:
        if char == "-":
            count_up = 0
            while arithmatic.index(char)+2+count_up < len(arithmatic) and arithmatic[arithmatic.index(char)+2+count_up] not in BIDMAS:
                count_up += 1
            minchar = min(arithmatic.index(char)+2+count_up, len(arithmatic))
            sub1 = arithmatic[arithmatic.index(char)+1:minchar]
            print(sub1)
            count_down = 0
            if arithmatic.index(char) == 1:
                sub2 = arithmatic[0]
            else:
                while arithmatic.index(char)-2-count_down < 0 and arithmatic[arithmatic.index(char)-2-count_down] not in BIDMAS:
                    count_down += 1
                sub2 = arithmatic[arithmatic.index(char)-1-count_down:arithmatic.index(char)]
            print(sub2)
            replacement = arithmatic[arithmatic.index(char)-1-count_down:minchar]
            print(replacement)
            arithmatic = arithmatic.replace(str(replacement), str(int(int(sub2) - int(sub1))))
            print(arithmatic)
    #print(arithmatic)
    #print("pos_neg_end", pos_neg)
    print("final:", int(arithmatic) * int(pos_neg))




string_calc("-3*-3")
string_calc("3*-3")

# # (1*3)+5-(4*-10)
string_calc("3/-1+5-4*10000*-10")
string_calc("1+3+5-4*10/2")
string_calc("1-3+5-4000*10000+2*2")
