total = 1
adding = 2
start_amount = 1
len_side = 1
while len_side < 1001:
	len_side += 2
	for i in [1,2,3,4]:
		start_amount += adding
		total += start_amount
	adding += 2

print total

