value = ''
count = 0
while len(value) < 1000001:
	count += 1
	value += str(count)

print value[11]
print int(value[0]) * int(value[9]) * int(value[99]) * int(value[999]) * int(value[9999]) * int(value[99999]) * int(value[999999])
