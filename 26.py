# since 1/d has the same number of recurring digits as 1/(2d), start at 500
# probably a prime number

import math

maxn = 0
maxl = 0

for i in range(500,1000):
    remainders = []
    r = 1
    while True:
        while i>r:
            r *= 10
        r = r % i
        if r in remainders or r == 0:
            break
        remainders.append(r)
        #print(r)

    print(maxl,maxn)
    if len(remainders) > maxl:
        maxn = i
        maxl = len(remainders)

print(maxl,maxn)


