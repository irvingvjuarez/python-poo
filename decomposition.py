from utils import conditionalProp

class Retina:
	def __init__(self, type):
		self.type = type

class Computer:
	def __init__(self, config = {}):
		self.brand = conditionalProp(config, "brand", "Apple")
		self.chip = conditionalProp(config, "chip", "Intel")
		self.memory = conditionalProp(config, "memory", "32 MB")
		self.retina = conditionalProp(config, "retina", Retina("display"))

if __name__ == "__main__":
	compu = Computer({"brand": "ASUS"})
	print(compu.brand)
	print(compu.chip)