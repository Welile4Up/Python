# Function that takes in an artist name, album title and number of songs
def make_album(artist, title, number_songs=None):
    """Build a dictionary describing a music album."""
    dictionary = {
        'artist': artist.title(),
        'title': title.title(),
        }
    if number_songs:
        dictionary['number_songs'] = number_songs
    return dictionary

# Call the function with 3 combinations of artist and title
album = make_album('jock', 'blue')
print(album)

album = make_album('nathi', 'bokwe')
print(album)

album = make_album('seal', 'rose')
print(album)

# Call the function with a combination of artist, title and number of songs
album = make_album('nas', 'stillmatic', number_songs=10)
print(album)
