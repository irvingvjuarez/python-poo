def bubbleSort(arr):
	isSorted = all(item <= arr[index + 1] for index, item in enumerate(arr) if index <= len(arr) - 2)

	while (not isSorted):
		for index, item in enumerate(arr):
			if index <= len(arr) - 2:
				isCurrentGreater = True if item > arr[index + 1] else False
				if isCurrentGreater:
					nextItem = arr[index + 1]
					arr[index] = nextItem
					arr[index + 1] = item
			else:
				break

		isSorted = all(item <= arr[index + 1] for index, item in enumerate(arr) if index <= len(arr) - 2)

	return arr

if __name__ == "__main__":
	arr = [6,5,3,1,8,7,2,4]

	print(
		bubbleSort(arr)
	)