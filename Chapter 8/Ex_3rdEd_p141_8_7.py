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
