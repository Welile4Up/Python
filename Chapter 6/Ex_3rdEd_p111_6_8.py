dog = {"animal_kind": "canine", "owner_name": "Steve Bell"}    #Defined a dictionary called dog that stores values for animal kind and owner name. 
cat = {"animal_kind": "feline", "owner_name": "John Little"}    #Defined a dictionary called cat that stores values for animal kind and owner name.         
fish = {"animal_kind": "piscine", "owner_name": "Bob Wilmore"}    ##Defined a dictionary called fish that stores values for animal kind and owner name.     

pets = [dog, cat, fish]    #Stored each of the above three dictionaries in a list called pets

for pet in pets:    #Loop through the pets list and print out each pets information
    print(pet)