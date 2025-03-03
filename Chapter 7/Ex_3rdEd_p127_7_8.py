sandwich_orders = ["cheese and tomato", "bacon and egg", "tuna mayo"]
finished_sandwiches = []

# Loop through the list of each sandwich order and print a message
for sandwich_order in sandwich_orders:
    print(f"\nI am making your {sandwich_order} sandwich.")

# Move completed sandwiches to the list of finished_sandwiches 
while sandwich_orders:
    busy_order = sandwich_orders.pop()

    finished_sandwiches.append(busy_order)

# Display message listing each sandwich that was made
print("\nThe following sandwiches have been made: ")
for finished_sandwich in finished_sandwiches:
    print(finished_sandwich)

