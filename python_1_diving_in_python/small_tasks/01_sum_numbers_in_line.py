import sys
digit_string = sys.argv[1]

sum = 0

for char in digit_string:
    number = int(char)
    sum += number

print(sum)