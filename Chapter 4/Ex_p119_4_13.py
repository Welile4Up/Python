simple_foods = ("bread", "eggs", "potatoes", "chicken", "salad")

for simple_food in simple_foods:
    print(simple_food)

# simple_foods[0] = "maize"
# print(simple_food[0])   #TypeError: 'tuple' does not support item assignment in line 6

simple_foods = ("maize", "hommus", "potatoes", "chicken", "salad")

print("\nRevised menu:")
for simple_food in simple_foods:
    print(simple_food)

