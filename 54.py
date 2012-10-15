def test_boat(values):
	if len(set(values)) == 2:
		if not(test_4(values)):
			return True
	return False

def test_pair(values):
	testers = {}
	for value in values:
		testers[value] = 0
	for value in values:
		if testers[value]:
			testers[value] += 1
		else:
			testers[value] = 1
	for i in testers:
		if testers[i] == 2:
			if not test_2pair(values) and not test_boat(values):
				return True
	return False

def test_2pair(values):
	testers = {}
	for value in values:
		testers[value] = 0
	for value in values:
		if testers[value]:
			testers[value] += 1
		else:
			testers[value] = 1
	count = 0
	for i in testers:
		if testers[i] == 2:
			count += 1
	if count == 2:
		return True
	return False
	

def test_straightflush(hand):
	return test_flush(get_suits(hand)) and test_straight(get_values(hand))

def test_flush(suits):
	if len(set(suits)) == 1:
		return True
	return False

def test_straight(values):
	values.sort()
	if values == [2, 3, 4, 5, 14]:
		return True
	for i in range(len(values) - 1):
		if not values[i] + 1 == values[i + 1]:
			return False
	return True

def test_3(values):
	testers = {}
	for value in values:
		testers[value] = 0
	for value in values:
		if testers[value]:
			testers[value] += 1
		else:
			testers[value] = 1
	for i in testers:
		if testers[i] == 3:
			if not test_boat(values):
				return True
	return False

def test_4(values):
	testers = {}
	for value in values:
		testers[value] = 0
	for value in values:
		if testers[value]:
			testers[value] += 1
		else:
			testers[value] = 1
	for i in testers:
		if testers[i] == 4:
			return True
	return False

def get_values(hand):
	values = []
	letters = {'A':14, 'K':13, 'Q':12, 'J':11, 'T':10}
	for card in hand:
		try:
			values.append(int(card[0]))
		except:
			values.append(int(letters[card[0]]))
	return values

def get_suits(hand):
	suits = []
	for card in hand:
		suits.append(card[1])
	return suits

def rank_hand(cards):

	if test_straightflush(cards):
		print "STRAIGHTFLUSH!"
	
	#test for flush
	if test_flush(get_suits(cards)):
		print "FLUSH!"

	#test for straight
	if test_straight(get_values(cards)):
		print "STRAIGHT!"
	
	#test for four of a kind
	if test_4(get_values(cards)):
		print "4 of a kind!"

	#test for boat
	if test_boat(get_values(cards)):
		print "BOAT!"

	if test_3(get_values(cards)):
		print "3 of a kind!"

	if test_2pair(get_values(cards)):
		print "2 pair!"

	if test_pair(get_values(cards)):
		print "one pair!"
	
	


'''
with open("poker.txt", 'r') as f:
	line = f.readline()
	cards = line.split(" ")
'''
	

rank_hand(['5D', '5D', '5H', '9D', '7C'])
rank_hand(['AD', '2D', '3D', '4C', '5D'])
