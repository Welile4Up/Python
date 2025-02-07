#Version 1
alien_color = "green"    #Assign the value green to the variable alien_color

if alien_color == "green":    #if test checks to see if the value of alien_color is green
    print("Player has won 5 points for shooting the green alien.")    #It is green, so this print() call is executed
elif alien_color == "yellow":    #Because test in line 3 passed, this elif test is skipped
    print("Player has won 10 points for shooting the yellow alien.")    
else:    #This else block is skipped 
    print("Player has won 15 points for shooting the red alien.")   

#version 2
alien_color = "yellow"    #Assign the value yellow to the variable alien_color

if alien_color == "green":    #if test fails 
    print("Player has won 5 points for shooting the green alien.")    #code block not executed
elif alien_color == "yellow":    #elif test passes because alien_color is yellow
    print("Player has won 10 points for shooting the yellow alien.")    #This print() call is executed    
else:    #This else block is skipped 
    print("Player has won 15 points for shooting the red alien.") 

#Version 3
alien_color = "red"    #Assign the value red to the variable alien_color

if alien_color == "green":    #if test fails 
    print("Player has won 5 points for shooting the green alien.")    #code block not executed
elif alien_color == "yellow":    #elif test fails
    print("Player has won 10 points for shooting the yellow alien.")    #code block not executed    
else:    #if and elif tests failed, so code in else block is run 
    print("Player has won 15 points for shooting the red alien.")    #This print() call is executed


