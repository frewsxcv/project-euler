from math import sqrt

def is_prime(i):
    for prime in primes:
        if not i % prime:
            return False
        elif prime > sqrt(i):
            break
    return True

primes = [2]
i = 3
while i < 2000000:
    if is_prime(i):
        primes.append(i)
    i += 1
print(sum(primes))
