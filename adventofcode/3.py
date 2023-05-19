txt = open("C:/dev/adventofcode/3.txt")
backpack = txt.read().split('\n')
txt.close()

letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
res = 0

for el in backpack:
    p1 = el[0:int(len(el) / 2)]
    p2 = el[int(len(el) / 2):len(el)]

    res += letters.index(''.join(set(p1).intersection(p2))) + 1

print(res)

# round 2

txt = open("C:/dev/adventofcode/3.txt")
backpack = txt.read().split('\n')
txt.close()

letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
res = 0

for i in range(0, len(backpack) - 1, 3):
    group = backpack[i:i+3]
    s1 = set(group[0]).intersection(set(group[1]))
    s2 = s1.intersection(set(group[2]))
    res += letters.index(''.join(s2)) + 1

print(res)
