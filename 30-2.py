results = []
for i in xrange(2, 999999):
	if i == sum([int(x)**5 for x in str(i)]):
		results.append(i)

print results
print sum(results)
