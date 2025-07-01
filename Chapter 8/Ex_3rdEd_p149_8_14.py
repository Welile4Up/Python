def make_car(manufacturer, model, **options):
    """Build a dictionary containing information about a car."""
    my_car = {
        'manufacturer': manufacturer.title(),
        'model': model.title(),
        }
    for option, value in options.items():
        my_car[option] = value

    return my_car

my_volksie = make_car('volkswagen', 'golf', color='white', leather_seats=False)
print(my_volksie)

my_merc = make_car('mercedes-benz', 'c-class', color='black', leather_seats=True)
print(my_merc)