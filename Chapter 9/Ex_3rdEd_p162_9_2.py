class Restaurant:
    """An attempt to model a restaurant."""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize restaurant_name and cuisine_type attributes."""
        self.restaurant_name = restaurant_name.title()
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Provide a description of the restaurant."""
        message = f"{self.restaurant_name} makes the best {self.cuisine_type}."
        print(f"\n{message}")

    def open_restaurant(self):
        """Indicate that the restaurant is open."""
        message = f"{self.restaurant_name} is open for business. Welcome!"
        print(f"\n{message}")

# Create three different instances from the class and call describe_restaurant for each
royale = Restaurant('the royale', 'burgers')
royale.describe_restaurant()

paolo = Restaurant('Paolo', 'pizza')
paolo.describe_restaurant()

chop_suey = Restaurant('chop suey', 'chinese food')
chop_suey.describe_restaurant()