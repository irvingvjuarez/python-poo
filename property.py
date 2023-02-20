class VotingBooth:
  def __init__(self, id, states):
    self._id = id
    self._states = states
    self._region = None

  @property
  def region(self):
    return self._region

  @region.setter
  def region(self, region):
    if region.lower() in list(map(lambda state: state.lower(), self._states)):
      self._region = region.capitalize()
    else:
      raise ValueError(f"Region {region} not valid")


if __name__ == "__main__":
  booth = VotingBooth(123, ["Ciudad de México", "Monterrey", "Guadalajara", "Oaxaca"])
  print(booth.region)

  booth.region = "Oaxaca"
  print(booth.region)