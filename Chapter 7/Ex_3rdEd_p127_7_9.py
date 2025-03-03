# List of sandwich orders, including multiple pastrami orders
sandwich_orders = ["cheese and tomato", "pastrami", "bacon and egg", "pastrami", "tuna mayo", "pastrami"]

finished_sandwiches = []

# Loop through the list of ordered sandwiches
print("\nThe following sandwiches have been ordered: ")
for sandwich_order in sandwich_orders:
    print(sandwich_order)

# Print message that there is no pastrami 
print("\nUnfortunately, the deli has run out of pastrami.")

# Remove all pastrami from sandwich_orders list
while "pastrami" in sandwich_orders:
    sandwich_orders.remove("pastrami")

# Move completed sandwiches to the list of finished_sandwiches
while sandwich_orders:
    busy_order = sandwich_orders.pop()

    finished_sandwiches.append(busy_order)

# Display message listing each sandwich that was made
print("\nThe following sandwiches have been made: ")
for finished_sandwich in finished_sandwiches:
    print(finished_sandwich)
