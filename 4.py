palins = []
for i in xrange(100, 1000):
    for x in xrange(100, 1000):
        y = x * i
        if str(y)[::-1] == str(y):
			palins.append(y)

palins = sorted(palins)
print palins[-1]
