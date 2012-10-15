def triangle(n):
	return n * (n + 1) / 2

def pentagonal(n):
	return n * (3 * n - 1) / 2

def hexagonal(n):
	return n * (2 * n - 1)

tris = [triangle(i) for i in range(1, 100000)]
pents = [pentagonal(i) for i in range(1, 100000)]
hexes = [hexagonal(i) for i in range(1, 100000)]

print list(set(tris) & set(pents) & set(hexes))
