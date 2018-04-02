# comment with ctrl+k ctrl+c
# uncomment with ctrl+k ctrl+u

# switch first number that is decending from right to left with next higher number from numbers on right
# sort numbers after switched

import math

order = [0,1,2,3,4,5,6,7,8,9]
switch = 8

print(order[:8])
print(list(str(order[switch])).extend([3,4]))

order.sort()



def nextHigher(n,arr):
    arr.sort()
    for i in arr:
        if i>n:
            return i

for i in range(1,1000000):
    for n in range(len(order)-1,0-1,-1):
        if(n+1 != len(order) and order[n] < order[n+1]):
            preorder = order[:n]
            preorder.append(nextHigher(order[n],order[n+1:]))
            lastorder = order[n+1:]
            lastorder.remove(preorder[-1])
            lastorder.append(order[n])
            lastorder.sort()
            preorder.extend(lastorder)
            order = preorder

            break
        m = n
    if(i % 1000 == 0):
        print(order)

print(order)
