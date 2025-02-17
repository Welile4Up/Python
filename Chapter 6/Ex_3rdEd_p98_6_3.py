coding_words = {    #defined the dictionary coding_words, with programming words and their meanings as key-value pairs
    "variable": "container for storing data values",
    "list": "used to store multiple items in a variable",
    "string": "sequence of characters enclosed in either single or double quotes",
    "loop": "allows block of code to be executed repeatedly until a certain condition is met",
    "dictionary": "data structure that stores items in key-value pairs",
    }

word_1 = coding_words["variable"]    #In line 9 to 18, we use the programming word keys to pull their respecitve meaning values in the dictionary. We assign these respective meanings to the new variables word_1 to word_5. We use each of these new variables to print() call and output the programming word, a colon and it's meaning.    
print(f"variable: {word_1}")
word_2 = coding_words["list"]
print(f"list: {word_2}")
word_3 = coding_words["string"]
print(f"string: {word_3}")
word_4 = coding_words["loop"]
print(f"loop: {word_4}")
word_5 = coding_words["dictionary"]
print(f"dictionary: {word_5}")

