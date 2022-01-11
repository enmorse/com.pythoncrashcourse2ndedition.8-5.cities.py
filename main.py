# Write a function named describe_city() that accepts
# the name of a city and its country. The function should
# print a simple sentence, such as Reyjavik is in
# Iceland. Give the parameter for the country a default
# value. Call your function for the three different cities,
# at least one of which is not in the default country.

def describe_city(city, country="USA"):
    print(f"The city {city.title()} is in the Country of "
          f"{country}")


describe_city("san diego")
describe_city("st andrews", "Scotland")
describe_city("munich", 'Germany')
