txt = open("C:/dev/adventofcode/2.txt")
rps = txt.read()
txt.close()

res = 0

for r in rps.split('\n'):
    if r[2] == 'X':
        res += 1
        if r[0] == 'A':
            res += 3
        elif r[0] == 'C':
            res += 6
    elif r[2] == 'Y':
        res += 2
        if r[0] == 'A':
            res += 6
        elif r[0] == 'B':
            res += 3
    elif r[2] == 'Z':
        res += 3
        if r[0] == 'B':
            res += 6
        elif r[0] == 'C':
            res += 3

print(res)

# round 2

txt = open("C:/dev/adventofcode/2.txt")
rps = txt.read()
txt.close()

res = 0

for r in rps.split('\n'):
    if r[0] == 'A':
        if r[2] == 'X':
            res += 3
        elif r[2] == 'Y':
            res += 4
        elif r[2] == 'Z':
            res += 8
    elif r[0] == 'B':
        if r[2] == 'X':
            res += 1
        elif r[2] == 'Y':
            res += 5
        elif r[2] == 'Z':
            res += 9
    elif r[0] == 'C':
        if r[2] == 'X':
            res += 2
        elif r[2] == 'Y':
            res += 6
        elif r[2] == 'Z':
            res += 7

print(res)
