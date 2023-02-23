def flatDict(dictionary):
	hasSubDict = any(type(i) == dict for i in dictionary.values())

	while hasSubDict:
		for key, value in dictionary.items():
			if type(value) == dict:
				subDict = dictionary[key].copy()
				del dictionary[key]
				dictionary.update(subDict)
				break

		hasSubDict = any(type(i) == dict for i in dictionary.values())

	sortedDict = sorted(dictionary.items(), key=lambda x: x[0])
	return dict(sortedDict)

if __name__ == "__main__":
	dictionary = {
		"a": "Word",
		"b": "Second word",
		"c": {
			"e": "Party",
			"f": "Car",
			"g": {
				"h": "Clean"
			}
		},
		"d": "Cheers"
	}

	flattedDict = flatDict(dictionary)
	print(flattedDict)
