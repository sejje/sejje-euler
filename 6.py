'''
Find the difference between the sum of the
squares of the first one-hundred natural
numbers and the square of the sum
'''

def sum_squares(n):
	return sum(i * i for i in range(1, n+1))

def square_sum(n):
	return sum(range(1, n+1)) ** 2

print square_sum(100) - sum_squares(100)
