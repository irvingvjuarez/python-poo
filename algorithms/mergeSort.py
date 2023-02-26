def mergeSort(first, second):
	fLen = len(first)
	sLen = len(second)

	if fLen <= 1 or sLen <= 1:
		orderedLst = []

		for i in range(0, fLen + sLen + 1):
			try:
				fCurrent = first[0]
				sCurrent = second[0]

				if fCurrent < sCurrent:
					orderedLst.append(fCurrent)
					first.pop(0)
				else:
					orderedLst.append(sCurrent)
					second.pop(0)
			except IndexError:
				if len(first) == 0:
					orderedLst.extend(second)
					second.clear()
				else:
					orderedLst.extend(first)
					first.clear()

				break

		return orderedLst
	else:
		fHalf = fLen // 2
		sHalf = sLen // 2

		return mergeSort(
			mergeSort(first[:fHalf], first[fHalf:]),
			mergeSort(second[:sHalf], second[sHalf:])
		)

if __name__ == "__main__":
	arr = [6, 5, 3, 1, 8, 7, 2, 4]
	half = len(arr) // 2

	print(
		mergeSort(arr[:half], arr[half:])
	)