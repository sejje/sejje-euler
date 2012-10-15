record = 0
for a in range(1, 100):
	for b in range(1, 100):
		llist = list(str(a**b))
		ssum = sum([int(nnum) for nnum in llist])
		if ssum > record:
			record = ssum
print record
