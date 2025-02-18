cities = {
    "London": {
        "country": "England",
        "population": 6000000,
        "fact": "finance centre",
        },

    "Joburg": {
        "country": "South Africa",
        "population": 3000000,
        "fact": "city of gold",
        },

    "Sydney": {
        "country": "Australia",
        "population": 4000000,
        "fact": "golden beaches",
        },

    }

for city_names, city_notes in cities.items():
    print(f"\nCity: {city_names}")
    for key, value in city_notes.items():
        print(f"\t{key.title()}: {value}")