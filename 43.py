from eulertools import is_pandigital
from itertools import permutations

perms = permutations(str(1234567890))

total = 0
for i in perms:
	if not int(i[1] + i[2] + i[3]) % 2:
		if not int(i[2] + i[3] + i[4]) % 3:
			if not int(i[3] + i[4] + i[5]) % 5:
				if not int(i[4] + i[5] + i[6]) % 7:
					if not int(i[5] + i[6] + i[7]) % 11:
						if not int(i[6] + i[7] + i[8]) % 13:
							if not int(i[7] + i[8] + i[9]) % 17:
								print i
								total += int(''.join(i))
print total
		
