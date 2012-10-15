denominations = [200, 100, 50, 20, 10, 5, 2, 1]
target = 200
ways = [1] + [0]*target

for coin in denominations:
	for i in xrange(coin, target+1):
		ways[i] += ways[i-coin]
print ways[200]
