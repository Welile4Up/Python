age = 21    #variable age is set at a value of 21

if age < 2:    #if test fails
    print("This person is a baby.")
elif age >= 2 and age < 4:    #first elif test fails
    print("This person is a toddler.") 
elif age >= 4 and age < 13:    #second elif test fails
    print("This person is a kid.")
elif age >= 13 and age < 20:    #third elif test fails
    print("This person is a teenager.")
elif age >= 20 and age < 65:    #fourth elif test passes because age value is 21, which is greater than 20 and less than 65
    print("This person is an adult.")    #This print() call is executed
else:    #This else block is skipped 
    print("This person is an elder.")