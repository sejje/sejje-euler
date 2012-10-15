'''
Project Euler Problem 17

Calculate the number of letters used to write
out (in words) all the numbers from one to
one-thousand.

Spaces and dashes not included
'''

def number_lookup(num):
	#Pre-set the value (length) of words based on
	#base-10 and number

	ones = {'1':'one', '2':'two', '3':'three', '4':'four', '5':'five', '6':'six', '7':'seven', '8':'eight', '9':'nine', '10':'ten', '11':'eleven', '12':'twelve', '13':'thirteen', '14':'fourteen', '15':'fifteen', '16':'sixteen', '17':'seventeen', '18':'eighteen', '19':'nineteen'}

	tens = {'20':'twenty', '30':'thirty', '40':'forty', '50':'fifty', '60':'sixty', '70':'seventy', '80':'eighty', '90':'ninety'}

	others = {'100':'hundred and', '1000':'one thousand'}


	numstr = str(num)
	numlen = len(numstr)
	if num < 20:
		print ones[numstr]
		return ones[numstr]
	if numlen == 2:
		if numstr[1:2] == '0':
			print tens[numstr]
			return tens[numstr]
		local_tens = tens[str(int(numstr[0:1]) * 10)]
		local_ones = ones['%s' % numstr[1:2]]
		print '%s %s' % (local_tens, local_ones)
	if numlen == 3:
		#find hundreds
		hundreds_local = ones[numstr[0:1]] + ' hundred and '

		if numstr[2:3] == '0':
			print tens[numstr]
			return tens[numstr]
		local_tens = tens[str(int(numstr[1:2]) * 10)]
		local_ones = ones['%s' % numstr[2:3]]
		print '%s %s %s' % (hundreds_local, local_tens, local_ones)
	if numlen == 4:
		numstr = others['1000']

	return numstr

total = 0
for i in range (1, 105):
	total += len(number_lookup(i))

print total
