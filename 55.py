from palindrome import palindrome

def iterate(n):
	#Create iteration of n according to rules of Euler 55
	#Basically concactenate a number with its reverse like 19 + 91
	return n + int(str(n)[::-1])

def total_iterations(n):
	#count iterations of n that it takes to make a palindrome
	n = iterate(n)
	count = 1
	for i in range(1, 50):	
		#according to rules, stop at 50 or you've gone too far
		if not palindrome(str(n)):
			n = iterate(n)
			count += 1
	return count

total = 0
for i in range(1, 10000):
	iters = total_iterations(i)
	if iters == 50:
		total += 1
print total
