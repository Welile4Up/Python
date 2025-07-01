# p136 8.3
def make_shirt(size, message):
    """Summary of shirt size and message to be printed on it."""
    print(f"\nThis is a size {size} t-shirt.")
    print(f'The printed message will be, "{message}"')

make_shirt('small', 'Coding is great!')
make_shirt(size='large', message="Indentation helps.")

# p141 8.6
# Function that takes in the name of a city and its country
def city_country(city, country):
    """Return a string with the format of 'City, Country'."""
    return f"{city.title()}, {country.title()}"

# Call the function with three city-country pairs
city = city_country('barcelona', 'spain')
print(city)

city = city_country('harare', 'zimbabwe')
print(city)

city = city_country('tokyo', 'japan')
print(city)

# p141 8.7
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

