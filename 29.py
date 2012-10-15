integers = []
for i in range(2, 101):
	for x in range(2, 101):
		integers.append(i**x)
print len(set(integers))
