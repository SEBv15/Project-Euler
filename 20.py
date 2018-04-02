import math

result = 0

for digit in list(str(math.factorial(100))):
    result += int(digit)

print(result)