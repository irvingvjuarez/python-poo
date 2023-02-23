def flatList(lst):
	hasSubList = any(type(i) == list for i in lst)

	while hasSubList:
		for index, item in enumerate(lst):
			if type(item) == list:
				subLst = lst[index].copy()
				del lst[index]
				lst += subLst
				break

		hasSubList = any(type(i) == list for i in lst)

	return lst

if __name__ == "__main__":
	lst = [1,23,4,5, [4,5,6,[1,2,42,6]]]
	flattedLst = flatList(lst)
	print(flattedLst)