pizzas = ["salami", "chicken", "bacon"]
friend_pizzas = pizzas[:]

pizzas.append("pineapple")
friend_pizzas.append("pepperoni")

print("My favorite pizzas are:")
for pizza in pizzas:
    print(pizza)

print("\nMy friend's favorite pizzas are:")
for friend_pizza in friend_pizzas:
    print(friend_pizza)