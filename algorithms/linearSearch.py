import random

def linearSearch(items, target):
	result = False

	for item in items:
		if item == target:
			result = True
			break

	return result


if __name__ == "__main__":
	size = int( input("What's the size of the list ") )
	target = input("What number are you looking for? ")
	items = [random.randint(0, 100) for i in range(size)]

	res = linearSearch(items, target)
	resultText = "is" if res else "is not"

	print(items)
	print(f"The target {target} {resultText} in the list")
