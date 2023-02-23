import random

def binarySearch(items, target):
	if len(items) == 1:
		return True if items[0] == target else False

	items.sort()

	halfValue = round(len(items)/2)
	head = items[:halfValue]
	tail = items[halfValue:]

	if head[-1] >= target:
		return binarySearch(head, target)

	return binarySearch(tail, target)


if __name__ == "__main__":
	size = int(input("What's the size of the list? "))
	target = int(input("What's the target? "))
	items = [random.randint(0, 100) for i in range(size)]

	res = binarySearch(items, target)

	print(items)
	print(res)