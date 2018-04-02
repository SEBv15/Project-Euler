# find primes between 1000 and 9999

import math
import itertools

primes = [2]
bprimes = []
for i in range(3,9999,2):
    notp = False
    for j in primes:
        if(i % j == 0):
            notp = True
            break
    for j in range(primes[-1],int(math.sqrt(i))):
        if(j % 2 == 1):
            if(i % j == 0):
                notp = True
                break
    if not notp:
        primes.append(i)
        if(i>1000):
            bprimes.append(i)

primes = bprimes

pairs = {}

for n in primes:
    key = list(str(n))
    key.sort()

    if not "".join(key) in pairs:
        pairs["".join(key)] = []
    pairs["".join(key)].append(n)

print(pairs)

found = []

for pair in pairs:
    if(len(pairs[pair]) >= 3):
        for combo in itertools.combinations(pairs[pair],3):
            if(abs(combo[0] - combo[1]) == abs(combo[1] - combo[2])):
                found.append(combo)

print("")
print(found)

print("\n"+", ".join(["".join([str(n) for n in d]) for d in found]))




