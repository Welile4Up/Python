#Define a prompt that tells the user their two options: entering a topping of choice or entering the quit value.
prompt = "\nPlease enter a pizza topping of your choice:"
prompt += "\nEnter 'quit' to confirm you are done selecting toppings. "

#Set up a while loop asking users to enter toppings of choice until they enter "quit".
while True:    
    topping = input(prompt)    #Set up a variable topping to store the value the user enters.

    if topping == "quit":    #When user enters quit, the break staement runs, causing Python to exit the loop.
        break
    else:
        print(f"{topping.title()} topping has been added to your pizza.")    #If "quit" is not entered by user, this print() call will be executed.


