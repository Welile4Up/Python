favorite_places = {    #Defined a dictionary that holds information about people and their favorite places
    "Jeff": ["Joburg", "Cape Town", "Durban"],    #In line 2 to 6, the people's names are keys and the associated values are a list of their favorite places
    "Thabo": ["Maseru", "Roma", "Thaba Nchu"],
    "Steve": ["London", "Paris", "Madrid"],
    "Tebogo": ["Napoli", "Milos"],
    "Nandi": ["Atlanta", "Miami", "New Orleans", "Boston"], 
    }

for name, places in favorite_places.items():    #When we loop through the dictionary, we use the variable called name to hold each value from the dictionary. Each value will be a list.
    print(f"\n{name.title()}'s favorite places are:")
    for place in places:    #Inside the main dictionary loop, we use another for loop to run through each person's list of favorite places. 
        print(f"{place.title()}")

