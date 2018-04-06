def primes_sieve(n):
    """Return a list with prime numbers <= n"""
    out = list()
    sieve = [True] * (n+1)
    for p in range(2, n+1):
        if (sieve[p]):
            out.append(p)
            for i in range(p, n+1, p):
                sieve[i] = False
    return out

try:
    num = int(input("Search for primes until: "))
except ValueError:
    print("Couldn't parse input, only integers allowed.")
    quit()
for prime in primes_sieve(num):
    print("{} is a prime number".format(prime))
