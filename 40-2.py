value = ''
for i in range(1, 100000):
	value += str(i)

print len(value)
print value[11]
print int(value[0]) * int(value[9]) * int(value[99]) * int(value[999]) * int(value[9999]) * int(value[99999]) * int(value[999999])
