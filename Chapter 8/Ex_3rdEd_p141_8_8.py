def make_album(artist, title, number_songs=0):
    """Build a dictionary describing a music album."""
    dictionary = {
        'artist': artist.title(),
        'title': title.title(),
        }
    if number_songs:
        dictionary['number_songs'] = number_songs
    return dictionary

album = make_album('jock', 'blue')
print(album)

album = make_album('nathi', 'bokwe')
print(album)

album = make_album('seal', 'rose')
print(album)

album = make_album('nas', 'stillmatic', number_songs=10)
print(album)

# Prompts for user input of artist and title
artist_prompt = "\nWhat's the name of the artist? "
title_prompt = "What's the name of the album? "

# Present user with a quit option
print("Enter 'quit' if you'd like to stop.")

while True:
    artist = input(artist_prompt)
    if artist == 'quit':
        break

    title = input(title_prompt)
    if title == 'quit':
        break
    
    album = make_album(artist, title)
    print(album)

print("\nThank you for participating.")