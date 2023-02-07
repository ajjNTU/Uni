# List of Employees
# Given the list: employees = ['Li', 'John','Hannah','Alaa','Georgia']
#
employees = ['Li', 'John','Hannah','Alaa','Georgia']
# Write a program that finds the shortest employee name using linear search.
def shortest_name(namelist):
    length_of_shortest = len(namelist[0])
    shortest_index = 0
    for index, item in enumerate(namelist):
        if len(item) < length_of_shortest:
            length_of_shortest = len(item)
            shortest_index = index
    return [shortest_index, namelist[shortest_index]]


# employees = ['John','Hannah','Alaa','Georgia', 'Li']
# print(shortest_name(employees))


# Write a program that finds the longest employee name using linear search.
def longest_name(namelist):
    length_of_first = len(namelist[0])
    shortest_index = 0
    for index, item in enumerate(namelist):
        if len(item) > length_of_first:
            length_of_first = len(item)
            shortest_index = index
    return [shortest_index, namelist[shortest_index]]


# employees = ['Georgia','John','Hannah','Alaa', 'Li']
# print(longest_name(employees))


# Write a python program that creates two new lists: employees_desc and employees_asc that contain the
# strings from list employees sorted from longest to shortest (shortest to longest respectively), according to the
# number of characters of each string.
def desc_sort(names):
    sorted = []
    while names:
        sorted.append(names.pop(shortest_name(names)[0]))
    return sorted

#

print(desc_sort(["Jon","DWAdawdawda","adaddadwa","Jon", "joe", "poe", "hello"]))


def asc_sort(names):
    sorted = []
    while names:
        sorted.append(names.pop(longest_name(names)[0]))
    return sorted


# employees = ['Li', 'John','Hannah','Alaa','Georgia']
# print(asc_sort(employees))


# Extend your program by writing a function sort_strings(string_list,order) where string_list is a list of strings
# and order is a variable that indicates the order in which we want to have the list sorted.

def sort_strings(string_list, order):
    if order == "asc":
        return asc_sort(string_list)
    elif order == "des":
        return desc_sort(string_list)



print(sort_strings(["Jon","DWAdawdawda","adaddadwa","Jon", "joe", "poe", "hello"], "des"))
print(sort_strings(employees, "asc"))
print(sort_strings(["Jon","DWAdawdawda","adaddadwa","Jon", "joe", "poe", "hello"], "asc"))

# Test it using list employees.

# We want to add a new employee "Paul" to the list, while keeping it sorted. Propose an algorithm to do that
# without using the insert() method.


def insert_sorted(sorted_list, insert_val):
    pass
    #where to insert?
    # find index in sorted list where len[item] >= len(insert_val) <= len[item]
    # once that index number is known can do
    # mylist[0:index] + [insert value] + mylist[index:]


