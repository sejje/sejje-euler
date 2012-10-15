def divisible(num):
    for i in xrange(11, 21):
        if num % i:
            return False
    return True

def f1():
    x = 20
    while not divisible(x):
        x = x + 20
    return x

print (f1())
