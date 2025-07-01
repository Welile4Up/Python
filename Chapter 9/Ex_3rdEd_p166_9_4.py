class Restaurant:
    """An attempt to model a restaurant."""

    def __init__(self, restaurant_name, cuisine_type, number_served):
        """Initialize restaurant_name and cuisine_type attributes."""
        self.restaurant_name = restaurant_name.title()
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """Provide a description of the restaurant."""
        message = f"{self.restaurant_name} makes the best {self.cuisine_type}."
        print(f"\n{message}")

    def open_restaurant(self):
        """Indicate that the restaurant is open."""
        message = f"{self.restaurant_name} is open for business. Welcome!"
        print(f"\n{message}")

    def set_number_served(self, number_served):
        """Set the number of customers that have been served."""
        self.number_served = number_served

    def increment_number_served(self, additional_served):
        """Increment the number of customers served."""
        self.number_served += additional_served


restaurant = Restaurant('the royale', 'burgers', 0)
print(restaurant.restaurant_name)
print(restaurant.cuisine_type)

restaurant.describe_restaurant()
restaurant.open_restaurant()

print(f"\nNumber served: {restaurant.number_served}")
restaurant.number_served = 200
print(f"Number served: {restaurant.number_served}")

restaurant.set_number_served(300)
print(f"Number served: {restaurant.number_served}")

restaurant.increment_number_served(50)
print(f"Number served: {restaurant.number_served}")