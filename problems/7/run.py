def is_prime(i):
    for prime in primes:
        if not i % prime:
            return False
    return True

primes = [2]
i = 3
while len(primes) <= 10000:
    if is_prime(i):
        primes.append(i)
    i += 1
print(primes[10000])
