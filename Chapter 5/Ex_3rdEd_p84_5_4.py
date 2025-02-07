alien_color = "green"    #Assign the value green to the variable alien_color

if alien_color == "green":    #Python checks to see if the value of alien_color is green
    print("Player has won 5 points for shooting the alien.")    #It is green, so this print() call is executed
else:
    print("Player has won 10 points for shooting the alien.")    #This line of code will not be executed


alien_color = "blue"    #Assign the value blue to the variable alien_color

if alien_color == "green":    #Python checks to see if the value of alien_color is green
    print("Player has won 5 points for shooting the alien.")    #It is not green, so this line of code will not be executed
else:
    print("Player has won 10 points for shooting the alien.")    #Because conditional test in line 11 evaluated to False, this print() call will be executed

