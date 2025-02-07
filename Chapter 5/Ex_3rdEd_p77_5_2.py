#Tests for equality and inequality with strings
#Equality Test
animal = "lion"
print("Is animal == 'lion'? I think it will be True.")
print(animal == "lion")

animal = "lion"
print("Is animal == 'rhino'? I think it will be False.")
print(animal == "rhino")

#Inequality Test
selected_sauce = "barbeque"

if selected_sauce != "mustard":
    print("Not the mustard, thanks.")


selected_sauce = "barbeque"

if selected_sauce != "barbeque":
    print("Only the barbeque, please.")


#Tests using lower() method
car = "Porsche"
print("Is car == 'porsche'? I think it will be False.")
print(car == "porsche")

car = "Porsche"
print("Is car.lower() == 'porsche'? I think it will be True.")
print(car.lower() == "porsche")


#Numerical Tests
#Equality
age = 21
print("Is age == 21? I think it will be True.")
print(age == 21)

age = 21
print("Is age == 31? I think it will be False.")
print(age == 31)

#Inequality
age = 21
if age != 48:
    print("That is not the correct age. Please guess again.")

age = 48
if age != 48:
    print("That is not the correct age. Please guess again.")

#Greater Than
age = 28
print("Is age > 22? I think it will be True.")
print(age > 22)

age = 20
print("Is age > 22? I think it will be False.")
print(age > 22)

#Less Than
age = 18
print("Is age < 22? I think it will be True.")
print(age < 22)

age = 23
print("Is age < 22? I think it will be False.")
print(age < 22)

#Greater Than or Equal To
age = 35
print("Is age >= 30? I think it will be True.")
print(age >= 30)

age = 25
print("Is age >= 30? I think it will be False.")
print(age >= 30)

#Less Than or Equal To
age = 40
print("Is age <= 50? I think it will be True.")
print(age <= 50)

age = 60
print("Is age <= 50? I think it will be False.")
print(age <= 50)


#Tests using the and keyword and the or keyword
#and keyword
age_0 = 20
age_1 = 25
print("Is age_0 > 18 and age_1 > 18? I think it will be True.")
print(age_0 > 18 and age_1 > 18)

age_1 = 15
print("Is age_0 > 18 and age_1 > 18? I think it will be False.")
print(age_0 > 18 and age_1 > 18)

#or keyword
age_0 = 15
age_1 = 25
print("Is age_0 > 18 or age_1 > 18? I think it will be True.")
print(age_0 > 18 or age_1 > 18)

age_1 = 16
print("Is age_0 > 18 or age_1 > 18? I think it will be False.")
print(age_0 > 18 or age_1 > 18)


#Test whether item is in a list
animals = ["dog", "cat", "fish", "bird"]
print("Is 'dog' in the list animals? I think this is True.")
print("dog" in animals)

print("Is 'frog' in the list animals? I think this is False.")
print("frog" in animals)


#Test whether item is not in a list
animals = ["dog", "cat", "fish", "bird"]
test_animal = "baboon"

if test_animal not in animals:
    print(f"{test_animal.title()} is not part of the list named animals.")

test_animal = "dog"

if test_animal not in animals:
    print(f"{test_animal.title()} is not part of the list named animals.")


