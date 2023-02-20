class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def greet(self):
    name, age = self.name, self.age
    return f"Hi, my name is {name} and I'm {age} years old"