	
def lookup(string):
	f = open("words.txt", 'r')
	dictionary = f.read().split(",")
	for i in xrange(len(dictionary)): 
		dictionary[i - 1] = dictionary[i - 1].strip('"')
	print dictionary
	for i in xrange(1, len(string) + 1):
		print "trying %s" % string[0:i]
		if string[0:i] in dictionary:
			if not string[i:] == "":
				print "%s found in dict, looking up %s" % (string[0:i], string[i:])
				if lookup(string[i:]):
					return string[0:i] + lookup(string[i:])
	return None

print lookup("PICKYES")
