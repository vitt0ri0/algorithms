import sys
num_steps = int(sys.argv[1])

#test
# num_steps = 4

for i in range(num_steps):
    sharps = i + 1
    s = ""
    spaces = num_steps - sharps
    for j in range(spaces):
        s += " "
    for j in range(sharps):
        s += "#"
    print(s)