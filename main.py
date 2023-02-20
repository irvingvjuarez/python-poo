from instances import Person, Coordinate

# Person class
vladi = Person("Irving", 21)
dolphy = Person("Diego", 16)
chicha = Person("César", 23)

print(vladi.greet())
print(dolphy.greet())
print(chicha.greet())

# Coordinate class
coord = Coordinate(3, 30)
secondCoord = Coordinate(4, 8)

print(isinstance(coord, Coordinate))
# print(coord.getValues())
# print(coord.getValues())

# print(coord.distance(secondCoord))