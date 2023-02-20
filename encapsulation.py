'''
class Miles:
  def __init__(self, distance = 0):
    self.distance = distance

  def toKm(self):
    return self.distance * 1.609344
'''

class Miles:
  def __init__(self):
    self._distance = 0

  def toKm(self):
    return self._distance * 1.609344

  @property
  def distance(self):
    try:
      return self._distance
    except AttributeError as err:
      print(err)

  @distance.setter
  def distance(self, distance):
    if (distance < 0):
      raise ValueError(f"Value must be greater than or equal to 0")
    self._distance = distance

  @distance.deleter
  def distance(self):
    del self._distance


if __name__ == "__main__":
  airplane = Miles()
  print(airplane.distance)

  airplane.distance = 200
  print(airplane.distance)

  del airplane.distance
  print(airplane.distance)
