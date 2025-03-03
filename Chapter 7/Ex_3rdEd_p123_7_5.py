#Ask the user their age
prompt = "\nPlease enter your age:"
prompt += "\n(Enter '0' when you are finished.)"

while True:    # This while loop will continue asking the user to enter an age until they enter '0'
    age = input(prompt)
    age = int(age)

    #Check if user wants to exit the program
    if age == 0:    # When the user enters '0', the break statement will run, causing Python to exit the loop. 
        break

    #Determine the ticket price based on age
    if age < 3:
        print("The movie ticket is free.")
    elif 3 <= age <= 12:
        print("The movie ticket costs $10.")
    else:
        print("The movie ticket costs $15.") 

    

