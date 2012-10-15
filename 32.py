from eulertools import is_pandigital

products = []
for i in range(1, 999):
	for x in range(i, 9999):
		bigstr = str(i) + str(x) + str(x * i)
		if len(bigstr) == 9:
			if is_pandigital(int(bigstr)):
				products.append(x * i)			
				print i, x, x*i, sum(set(products))
print set(products)
print sum(set(products))
	
