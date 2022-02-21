
cities_file = open("cities.txt", "r")
file = open("reverse-cities.txt", "a")

cities = cities_file.readlines()
cities.reverse()
for city in cities:
    file.write(city)

cities_file.close()
file.close()