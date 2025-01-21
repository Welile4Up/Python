languages = ["German", "English", "French", "Japanese", "Portuguese", "Spanish", "Chinese"]

languages[4] = "Shangaan"
print(languages)

languages.append("Gaelic")
print(languages)

languages.insert(0, "Setswana")
print(languages)

del languages[2]
print(languages)

languages.pop()
print(languages)

languages.remove("Spanish")
print(languages)

languages.sort()
print(languages)

languages.reverse()
print(languages)

print(f"There are {len(languages)} languages in this updated list.")



 