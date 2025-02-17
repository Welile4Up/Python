#Start with the program from Exercise 6-1
Thabo_Mooki = {"first_name": "Thabo", "last_name": "Mooki", "age": 25, "city": "Pretoria"}    #Defined a dictionary called Thabo_Mooki that stores values for first name, last name , age and city

#Make two new dictionaries representing different people
James_Selfe = {"first_name": "James", "last_name": "Selfe", "age": 26, "city": "Durban"}
Sipho_Khumalo = {"first_name": "Sipho", "last_name": "Khumalo", "age": 28, "city": "Cape Town"}

#Store all three dictionaries in a list called people
people = [Thabo_Mooki, James_Selfe, Sipho_Khumalo]    #Stored each of the three dictionaries in a list called people

#Loop through the list and print everything you know about each person
for person in people:    #Loop through the people list and print out each person
    print(person)

