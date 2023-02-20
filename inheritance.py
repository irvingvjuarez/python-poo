class Rectangule:
  def __init__(self, width = 5, height = 5):
    self._width = width
    self._height = height
    self._area = width * height

  @property
  def area(self):
    return self._area

  def _updateArea(self):
    self._area = self._height * self._width

  @property
  def width(self):
    return self._width

  @width.setter
  def width(self, width):
    if width > 0:
      self._width = width
      self._updateArea()
    else:
      raise ValueError(f"{width} must be greater than or equal to zero")

  @property
  def height(self):
    return self._height

  @height.setter
  def height(self, height):
    if height > 0:
      self._height = height
      self._updateArea()
    else:
      raise ValueError(f"{height} must be greater than or equal to zero")


class Square(Rectangule):
  def __init__(self, side):
    super().__init__(side, side)


if __name__ == "__main__":
  # rect = Rectangule()
  # print(rect.width, rect.height, rect.area)

  # rect.width = 10
  # rect.height = 10
  # print(rect.width, rect.height, rect.area)

  sqr = Square(5)
  print(sqr.width, sqr.height, sqr.area)

  sqr.width = 10
  sqr.height = 20

  print(sqr.width, sqr.height, sqr.area)