# 1. Pride and  Prejudice
# First, download the text file. It is a plain text utf-8 version of Jane Austen's Pride and Prejudice provided by
# Project Gutenberg.
#
# Open and inspect the file in a text editor. Note the structure.

# Create a new python file files.py

# Write a python program that opens the book by following the steps:
# Create two variables: path and filename where path contains the path to your directory and filename the name of your
# text file.
import os
def openbook(path, filename):

    try:
        book = open(path + "\\" + filename, encoding='utf-8')
        for line in book.readlines():
                print(line)
    finally:
        book.close()

#print(os.path(book))
openbook(r"C:\Users\aj104\PycharmProjects", "pg1342.txt")

# try:
#     book1 = open(r"C:\Users\aj104\PycharmProjects\pg1342.txt", encoding='utf-8')
#     for line in book1.readlines():
#         print(line)
# finally:
#     book1.close()



# Open your file in read-only mode and read it line by line. You might need to use an encoding='UTF-8' argument.
# Use the os.path module in order to set-up the path to your file using the variables you defined in the previous step.
# [hint] There is a method that does this efficiently. Check out python's official documentation for help.
# Change your program to only read lines that contain the word "Chapter". How many chapters does the book have?
def chapters(path, filename):
    try:
        count = 0
        book = open(path + "\\" + filename, encoding='utf-8')
        for line in book.readlines():
            if line[0:7] == "Chapter" or line[0:7] == "CHAPTER":
                count += 1
        print("Chapters:", count)
    finally:
        book.close()


chapters(r"C:\Users\aj104\PycharmProjects", "pg1342.txt")
# [hint] Think of how you can use the in operator.

# Make sure you add a try/finally clause if you haven't already.
