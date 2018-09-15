import sys
import math

if len(sys.argv) > 3:
    a = int(sys.argv[1])
    b = int(sys.argv[2])
    c = int(sys.argv[3])

# test
# a = 1
# b = -3
# c = -4

D = math.sqrt(b * b - 4 * a * c)
x1 = (-b + D) / 2 * a
x2 = (-b - D) / 2 * a

print(int(x1))
print(int(x2))
