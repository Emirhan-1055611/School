#Opdracht 1 (Standaard rekenoperatoren)


# // = gedeeld door maar het rondt af naar beneden.
# ** = kwadrateren

from numbers import Integral


print(2 + 3)
print(2 - 3)
print(2 * 3)
print(2 / 3)
print(2 // 3)
print(2 ** 3)
print(3 + 2)
print(3 - 2)
print(3 * 2)
print(3 / 2)
print(3 // 2)
print(3 ** 2)

#Opdracht 2 (Haakjes)

print(23.95 * 32.9)
print(23.95 * 32.9 + 6)
print((23.95 * 32.9) + 6)
print(23.95 * (32.9 + 6))
print(23.95 / 32.9)
print(23.95 / 32.9 + 6)
print((23.95 / 32.9) + 6)
print(23.95 / (32.9 + 6))

#Opdracht 3 (Variabelen)

name = "John Doe"
print(name)

street = "Neverland Lane"
print(street)

items = 5
print(items)

price = 19.95
print(price)

student = 28
teachers = 3
seats = student + teachers
print(seats)

correct = student > teachers
print(correct)

incorrect = student > seats
print(incorrect)

line_character = '-'
line = line_character * 20
print(line)

#Opdracht 4 (IDLE)

city = "Rotterdam"
print(city)
type(city)

residents = 623652
print(residents)
type(residents)

area = 324.1
print(area)
type(area)

print(f"The city of {city} has {residents} on an area of {area} square kilometers")