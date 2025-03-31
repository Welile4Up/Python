def describe_city(city, country='Spain'):
    """Describing location of a city."""
    message = f"{city.title()} is in {country.title()}."
    print(message)

describe_city('barcelona')
describe_city('madrid')
describe_city('lisbon', 'portugal')