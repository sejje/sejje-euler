'''
Sort names.txt by alphabetical order

Work out alphabetical score for each name, multiply
by position in list to score each name.

Sum the name scores
'''

def sort_file(filename):
	with open(filename, 'r') as f:
		line = f.readline()
		names = line.split('","')
		names.sort()
	return names

def sort_file2(filename):
	with open(filename, 'r') as f:
		line = f.readline()
		names = []
		names.append(line)
		names.sort()
	return names


def score_name(name):
	values = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6, 'g':7, 'h':8, 'i':9, 'j':10, 'k':11, 'l':12, 'm':13, 'n':14, 'o':15, 'p':16, 'q':17, 'r':18, 's':19, 't':20, 'u':21, 'v':22, 'w':23, 'x':24, 'y':25, 'z':26}
	temp = list(name)
	total = 0
	for i in temp:
		total += values[i.lower()]
	return total

def score_all(name_list):
	total = 0
	for i in range(1, len(name_list)):
		#print name_list[i]
		score = score_name(name_list[i])
		score = score * i
		total += score
	return total


name_list = sort_file('names.txt')
print score_all(name_list)
