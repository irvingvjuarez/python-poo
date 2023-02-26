from bokeh.plotting import figure, output_file, show

if __name__ == "__main__":
	output_file("simple_chart.html")
	fig = figure()

	totalVals = int(input("How many variables do you wanna to chart? "))
	xVals = list(range(totalVals))
	yVals = []

	for x in xVals:
		val = int(input(f"Value Y for {x} "))
		yVals.append(val)

	fig.line(xVals, yVals, line_width=2)
	show(fig)