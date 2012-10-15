"""
By considering the terms in the Fibonacci sequence
whose values do not exceed four million, find the
sum of the even-valued terms.
"""

def create_fibonacci():
	"""
	function to create a list of the fibonacci sequence
	seeding 1 and 2 to start us off
	"""
	fibonacci = [1,2]
	while True:
		new = fibonacci[-1] + fibonacci[-2]
		if new > 4000000:
			break
		fibonacci.append(new)

	return fibonacci

def f1():
	fib = create_fibonacci()
	total = 0
	for i in fib:
		if ((i % 2) == 0):
			total += i
	return total

def f2():
    fibs = create_fibonacci()
    return sum(f for f in fibs if not f % 2)

print f1()
print f2()
