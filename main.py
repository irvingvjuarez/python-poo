from instances import Person, Coordinate

# Person class
vladi = Person("Irving", 21)
dolphy = Person("Diego", 16)
chicha = Person("César", 23)

print(vladi.greet())
print(dolphy.greet())
print(chicha.greet())

# Coordinate class
coord = Coordinate()
print(coord.getValues())

coord.changeValues(10, 10)
print(coord.getValues())