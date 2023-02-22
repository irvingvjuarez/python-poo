import time

currentNumber = 100

def factIteration(number):
	result = number

	for i in range(1, number):
		number -= 1
		result *= number

	return result

iterationStart = time.time()
iterationResult = factIteration(currentNumber)

iterationEnd = time.time()
iterationTotal = iterationEnd - iterationStart

print(f"Iteration time: {iterationTotal}, result: {iterationResult}")


def factRecursion(number, obj = {}):
	if number in obj:
		return obj[number]

	if number == 1:
		return number

	obj[number] = number * factRecursion(number - 1, obj)
	return obj[number]


recursionStart = time.time()
recursionResult = factRecursion(currentNumber)

recursionEnd = time.time()
recursionTotal = recursionEnd - recursionStart
print(f"Recursion time: {recursionTotal}, result: {recursionResult}")