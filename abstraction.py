class Washer:
  def __init__(self):
    pass

  def wash(self, temperature="cold", waterLevel="min", clothesType="clear"):
    self._fillWater(temperature)
    self._wash()

    self._fillWater(temperature)
    self._addSoup()
    self._dry()

  def _fillWater(self, temperature):
    print(f"Filling washer with water at {temperature} degrees")

  def _wash(self):
    print("Washing clothes")

  def _addSoup(self):
    print("Adding soup to the blend of clothes and water")

  def _dry(self):
    print("Drying clothes")


if __name__ == "__main__":
  washer = Washer()
  washer.wash()