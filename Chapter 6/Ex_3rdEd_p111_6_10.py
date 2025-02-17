favorite_numbers = {    #Defined a dictionary called favorite_numbers, that has five names and 5 lists of numbers as keys and values respectively
    "Thabo": [33, 43], 
    "Jabu": [68, 78, 98], 
    "Sipho": [15, 25, 35, 45], 
    "Rajesh": [28, 38, 48], 
    "Ricky": [6, 16],
    }    

for name, numbers in favorite_numbers.items():    #When we loop through the dictionary, we use the variable called name to hold each value from the dictionary.
    print(f"\n{name.title()}'s favorite numbers are:")
    for number in numbers:    #Inside the main dictionary loop, we use another for loop to run through each person's list of favorite numbers. 
        print(number)