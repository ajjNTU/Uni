luhn = int(input("Input a number from 0-9: "))
if luhn >=0 and luhn <5:
    print("Luhn Double is:", luhn*2)
elif luhn>4 and luhn<10:
    print("Luhn Double is:", luhn*2-9)
else:
    print("Enter a whole number from 0-9")