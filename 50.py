from eulertools import prime_list_numbers, isprime

primes = prime_list_numbers(1000000)
sums = []

record = (0, 0, 0)

for i in xrange(0, len(primes)):
    count = 1
    while count + i < len(primes):
        x = sum(primes[i:count])
        if x < 1000000:
            if isprime(x):
                if len(primes[i:count]) > record[1]:
                    record = (x , len(primes[i:count]))
                    print record
        count += 1
print record
