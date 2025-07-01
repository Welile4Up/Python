# First approach for calling function

import city_module

# Call the function with a city-country pair
city = city_module.city_country('barcelona', 'spain')
print(city)


# Second approach for calling function

from city_module import city_country

# Call the function with a city-country pair
city = city_country('barcelona', 'spain')
print(city)


# Third approach for calling function

from city_module import city_country as cc

# Call the function with a city-country pair
city = cc('barcelona', 'spain')
print(city)


# Fourth approach for calling function

import city_module as cm

# Call the function with a city-country pair
city = cm.city_country('barcelona', 'spain')
print(city)


# Fifth approach for calling function

from city_module import *

# Call the function with a city-country pair
city = city_country('barcelona', 'spain')
print(city)


