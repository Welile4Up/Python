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
