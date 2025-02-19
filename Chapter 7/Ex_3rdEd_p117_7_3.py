number = input("Please enter a number, and I'll tell you whether it's a multiple of 10 or not: ")
number = int(number)

if number % 10 == 0:
    print(f"\n{number} is a multiple of 10.")
else: 
    print(f"\n{number} is not a multiple of 10.")
