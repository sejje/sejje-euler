import time
from math import factorial as fact
start = time.time()

columns = 20
rows = 20

print fact(columns + rows) / (fact(columns) * fact(rows))

print time.time() - start
