from string import ascii_uppercase

def letter_value(letter):
	return ascii_uppercase.index(letter.upper()) + 1

def triangle(n):
	return n * (n + 1) / 2

tris = [triangle(i) for i in range(1, 100)]

count = 0
f = open("words.txt", "r")
words = [word.strip('"') for word in f.read().split(',')]
print words
for word in words:
	total = 0
	for letter in word:
		total += letter_value(letter)
	if total in tris:
		count += 1

print count
