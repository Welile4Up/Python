# #VERSION 1 - Conditional Test in the while statement to stop the loop

# #Define a prompt that tells the user their two options: entering a topping of choice or entering the quit value.
# prompt = "\nPlease enter a pizza topping of your choice:"
# prompt += "\nEnter 'quit' to confirm you are done selecting toppings. "

# topping = ""    #Variable topping has been set up as empty string, to keep track of whatever value the user enters.

# while topping != "quit":    # The value of topping is compared to "quit". If they are not the same, Python will enter the loop.     
#     topping = input(prompt)    # Python displays the prompt and waits for the user to enter their input. 
#                                # Whatever they enter is assigned to the topping variable.

#     #if test conducted to ensure the word "quit" is not printed as if it were a topping
#     if topping != "quit":    
#         print(f"{topping.title()} has been added to your pizza.")    #If user input is not "quit", this print() call is executed.


# #VERSION 2 - Active variable used to control how long loop runs 

# #Define a prompt that tells the user their two options: entering a topping of choice or entering the quit value.
# prompt = "\nPlease enter a pizza topping of your choice:"
# prompt += "\nEnter 'quit' to confirm you are done selecting toppings. "

# active = True    # Set the variable active to True so the program starts in an active state. 
# while active:    # As long as the active variable remains True, the loop will continue running.   
#     topping = input(prompt)    # Python displays the prompt and waits for the user to enter their input. 
#                                # Whatever they enter is assigned to the topping variable.

#     if topping == "quit":    # In the if statement we check the value of topping once the user enters their input.
#         active = False    # If the user entered "quit", we set active to False and the while loop stops.
#     else:    
#         print(f"{topping.title()} has been added to your pizza.")    #If the user input was not "quit", this print() call is executed.


#VERSION 3 - Break statement used to exit the loop when user enters "quit" value

#Define a prompt that tells the user their two options: entering a topping of choice or entering the quit value.
prompt = "\nPlease enter a pizza topping of your choice:"
prompt += "\nEnter 'quit' to confirm you are done selecting toppings. "

#Set up a while loop asking users to enter toppings of choice until they enter "quit".
while True:    
    topping = input(prompt)    #Set up a variable called topping to store the value the user enters.

    if topping == "quit":    #When user enters quit, the break statement runs, causing Python to exit the loop.
        break
    else:
        print(f"{topping.title()} has been added to your pizza.")    #If "quit" is not entered by user, this print() call will be executed.

