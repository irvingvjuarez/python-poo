def insercionSort(lst):
	for index, num in enumerate(lst):
		if index > 0:
			current = num
			subLst = reversed( lst[:index] )

			currentIndex = index

			for subIndex, subNum in enumerate(subLst):
				if current < subNum:
					lst[index - subIndex] = subNum
					currentIndex -= 1
				else:
					break

			lst[currentIndex] = current

	return lst

if __name__ == "__main__":
	print(
		insercionSort([7,3,2,9,8])
	)