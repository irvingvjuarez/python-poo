class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def greet(self):
    return f"Hi, my name is {self.name} and I'm {self.age} years old"