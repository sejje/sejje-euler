
count = 0
result = False
while result == False:
	count += 1
	if not count % 1000:
		#print count
		pass
	test = list(str(count))
	test2 = list(str(count * 2))
	test3 = list(str(count * 3))
	test4 = list(str(count * 4))
	test5 = list(str(count * 5))
	test6 = list(str(count * 6))
	test.sort()
	test2.sort()
	test3.sort()
	test4.sort()
	test5.sort()
	test6.sort()

	if test == test2 == test3 == test4 == test5 == test6:
		print "TRUETRUE"
		result = True
print count
