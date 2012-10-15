import time
start = time.time()

marked = [0] * 2000000 #create a grid of sorts
value = 3 #start at a value to be tested
s = 2 #s is the total being counted, start at 2 to eliminate testing 2
while value < 2000000: #loop thru all values
	if marked[value] == 0: #if this number isn't marked it's prime
		s += value #add prime to total
		i = value
		while i < 2000000: #mark multiples of this number in grid
			marked[i] = 1
			i += value
	value += 2 #increase testing values (only test odds)
print s, time.time() - start
