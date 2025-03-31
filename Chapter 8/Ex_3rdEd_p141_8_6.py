def city_country(city, country):
    """Return a string on the format of 'City, Country'."""
    return f"{city.title()}, {country.title()}"

city = city_country('barcelona', 'spain')
print(city)

city = city_country('harare', 'zimbabwe')
print(city)

city = city_country('tokyo', 'japan')
print(city)