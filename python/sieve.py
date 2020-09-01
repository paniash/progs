## Computerphile: Laziness in python
# Sieve of Erastosthenes

# Generator sequence
def nats(n):
    yield n
    yield from nats(n+1)

# Sieve function
def sieve(s):
    n = next(s)
    yield n
    yield from sieve(i for i in s if i%n != 0)

# generate the sieve elements
p = sieve(nats(2))

while next(p) < 100:
    print(next(p))

# Does not print 2
