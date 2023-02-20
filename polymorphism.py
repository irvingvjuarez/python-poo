class Person:
  def __init__(self, name):
    self._name = name

  def move(self):
    return "I am walking forward"

class Cyclist(Person):
  def __init__(self, name):
    super().__init__(name)

  def move(self):
    return "I am biking"


if __name__ == "__main__":
  dolphy = Person("Dolphy")
  print(dolphy.move())

  vladi = Cyclist("Irving")
  print(vladi.move())