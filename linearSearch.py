def linearSearch(items, target):
	result = False

	for item in items:
		if item == target:
			result = True
			break

	return result


print(linearSearch(["irv", "ces", "dieg", "mom", "dad", "aunt", "cousins", "irv"], "irv"))