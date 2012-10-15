import math

def pyth(a, b, c):
	if a**2 + b**2 == c**2:
		return True
	if b**2 + c**2 == a**2:
		return True
	if a**2 + c**2 == b**2:
		return True
	return False
	
def all_solutions(p):
    #find all possible side lengths for perimiter p
    #in a right angle triangle
	results = []
	for a in xrange(1, p / 2):
		for b in xrange(1, a):
			c = math.sqrt(a**2 + b**2)
			if a + b + c == p:
				results.append((a, b, c))
	return results

def get_record(max_num):
	record = (0, 0)
	for p in xrange(2, max_num, 2):
		if len(all_solutions(p)) > record[0]:
			record = (len(all_solutions(p)), p)
	return record

print "Record: %s triplets, p = %s" % get_record(1000)
