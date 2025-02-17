favorite_languages = {
 "jen": "python",
 "sarah": "c",
 "edward": "rust",
 "phil": "python",
 }

#Make a list of people who should take the favorite languages poll.
people = ["jen", "peter", "sarah", "bob", "edward", "phil"]

#Loop through the list of people who should take the poll.
for person in people:

    if person in favorite_languages.keys():
        print(f"{person.title()}, thank you for taking the poll.")

    if person not in favorite_languages.keys():
        print(f"{person.title()}, please respond to the poll.")

