def fib(n):
	if n < 2: return n
	
	current_fib, next_fib = 0, 1

	while n > 0:
		current_fib, next_fib = next_fib, current_fib + next_fib
		n -= 1
	
	return current_fib

import time
start = time.time()
print fib(100000), time.time() - start
