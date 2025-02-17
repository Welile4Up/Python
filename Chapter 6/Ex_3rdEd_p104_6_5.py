river_country = {
    "orange": "namibia",
    "nile": "uganda",
    "zambezi": "zambia", 
    }

#Use a loop to print a sentence about each river
rivers = ["orange", "nile", "zambezi"]    #Make a list of the keys from the river_country dictionary

for river in river_country.keys():    #Create a for loop that loops through the keys (ie rivers) in the dictionary

    if river in rivers:    #Inside the loop, check whether the river we're working with is in the list rivers. 
        country = river_country[river]    #We determine the country by using the name of the dictionary and the current value of river as the key.
        print(f"The {river.title()} River runs through {country.title()}.")

#Use a loop to print the name of each river included in the dictionary
for river in river_country.keys():
    print(river.title())

#Use a loop to print the name of each country included in the dictionary
for river in river_country.values():
    print(river.title())

# #Alternative solution
# for river in river_country.keys():   

#     if river in rivers:    
#         country = river_country[river]   
#         print(country.title())
