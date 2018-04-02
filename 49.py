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

# def combinations(n, list, combos=[]):
#     #list.sort()
#     # initialize combos during the first pass through
#     if combos is None:
#         combos = []

#     if len(list) == n:
#         # when list has been dwindeled down to size n
#         # check to see if the combo has already been found
#         # if not, add it to our list
#         if combos.count(list) == 0:
#             combos.append(list)
#             combos.sort()
#         return combos
#     else:
#         # for each item in our list, make a recursive
#         # call to find all possible combos of it and
#         # the remaining items
#         for i in range(len(list)):
#             refined_list = list[:i] + list[i+1:]
#             combos = combinations(n, refined_list, combos)
#         return combos

found = []

for pair in pairs:
    if(len(pairs[pair]) >= 3):
        for combo in itertools.combinations(pairs[pair],3):
            if(abs(combo[0] - combo[1]) == abs(combo[1] - combo[2])):
                found.append(combo)

print("")
print(found)

print("\n"+", ".join(["".join([str(n) for n in d]) for d in found]))




