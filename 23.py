import math

# get list of abundant numbers <28123-12
nums = []
numss = ""
for n in range(12,28123-12):
    factors = []
    for i in range(2,n//2):
        if(n % i == 0):
            factors.append(n)
    if sum(factors) <= n:
        numss += str(n) + "\n"
        #nums.append(n)

    if(n%1000 == 0):
        print(n)
    #    print(numss)

print(nums)

file = open("abundant-numbers-28111.csv","w")
file.write(numss)
file.close()