#favorite_languages.py ORIGINAL Version
favorite_languages = {
    "jen": "python",
    "sarah": "c",
    "edward": "rust",
    "phil": "python",
    }

language = favorite_languages["sarah"].title()    #We pull Sarah's favorite language from the dictionary and assign it to the variable language
print(f"Sarah's favorite language is {language}.")


#favorite_languages.py UPDATED Version
favorite_languages = {    #the values in the key-value pairs are now lists
    "jen": ["python", "java", "go"],    
    "sarah": ["c", "javascript"],
    "edward": ["rust", "c#", "ruby"],
    "phil": ["python", "php"],
    }

for name, languages in favorite_languages.items():    #When we loop through the dictionary, we use the variable called name to hold each value from the dictionary.
    print(f"\n{name.title()}'s favorite languages are:")
    for language in languages:    #Inside the main dictionary loop, we use another for loop to run through each person's list of favorite languages. 
        print(f"\t{language.title()}")