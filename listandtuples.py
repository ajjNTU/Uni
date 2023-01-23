# 1. Getting familiar with lists and tuples
# Write a function that takes as parameter a tuple (values, element) which returns True if the element a is present in
# the list values, and False if not.
def iselementinvalue(values = ("hey","you"), element = "h"):
    for i in range(len(values)):
        j = 0
        while j < len(values[i]):
            if values[i][j] == element:
                print(element, "Was found in", values[i], "from Tuple", values)
                j = len(values[i])
            else:
                #print(element, "Was not found in", values[i])
                j += 1


iselementinvalue()
iselementinvalue(("noo","letter next to j and g","found"), "h")
iselementinvalue(("hhh","hey","sexeh",".....h","!h!"), "h")
iselementinvalue(("hhh","hey","sexeh",".....h","!h!"), "n")

# Write a function removeDuplicates(values) that finds and removes duplicate elements from list values. [hint] think of
# how you can use logical operators.
def removeDuplicates(values):
    # print(len(values))
    i = 0
    while i < len(values)-1:
        j = i + 1
        while j < len(values):
            # print(values)
            if values[i] == values[j]:
                # print("Removing: ", values[j], "j is", j, "because matches", values[i], "i is", i)
                values.remove(values[j])
                j = i + 1
            else:
                # print("OK: ", values[i], "i is", i, "and", values[j],  "j is", j,  "don't match")
                j += 1
        i += 1
    print("Final List:", values)
    return values


removeDuplicates( ["oranges", "oranges", "apple", "bananas", "organges"] )
removeDuplicates( ["oranges", "oranges", "apple", "bananas", "organges", "bananas"] )
removeDuplicates( ["oranges", "oranges", "apple", "bananas", "organges", "addition","apple", "apple", "apple", "bananas","bananas","bananas", "organges", "random"] )
# Write a function commonElements(list1,list2) which finds and returns all common elements between list1 and list2.
def commonElements(list1, list2):
    common = []
    i = 0
    # print(len(list1))
    # print(len(list2))
    # print(list1[3])
    while i < len(list1):
        j = 0
        while j < len(list2):
            if list1[i] == list2[j]:
                #print("Added", list1[i], "to common elements")
                common.append(list1[i])
                j += 1
            else:
                j += 1
        i += 1
    # print(common)
    return common


#commonElements([1,2,3,4], [4,5,6,7])

#commonElements([1,2,3,4], [1,2,2,3])

removeDuplicates(commonElements([1,2,3,4], [1,2,2,3]))
removeDuplicates(commonElements([4,4,4,4], [1,2,2,3]))
removeDuplicates(commonElements([1,2,2,3], [1,2,2,3]))
removeDuplicates(commonElements([1,2,3,4,5,6,7,8,9,10], [1,2,2,3,4,5,6,10]))

# Write a function myNumbers(values) that takes as parameter a list of integers values, and returns a list of tuples.
# Each tuple contains an integer and either 'odd' or 'even',
# Example:
# myNumbers([3,6,1,12]) should return [(3,'odd'),(6,'even'),(1,'odd'),(12,'even')]
def myNumbers(values):
    numbersoddeven = []
    for i in range(len(values)):
        if values[i]%2 == 0:
            numbersoddeven.append((values[i], 'even'))
        else:
            numbersoddeven.append((values[i], 'odd'))
    print(numbersoddeven)


myNumbers([3,6,1,12])
myNumbers([3,6,1,12])
myNumbers([-3,6,-1,12])


# Write in python function descending (n, m) which returns a list of integers from integer n to m (both inclusive) in
# descending order. Example: descending (2, 4) should return [4, 3, 2].
def descending(num1,num2):
    list = []
    for i in range(max(num1,num2),min(num1,num2)-1, -1):
        list.append(i)
    print(list)
    return list


descending(2,4)
descending(4,49)


