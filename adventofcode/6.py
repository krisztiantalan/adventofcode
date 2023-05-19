with open("C:/dev/adventofcode/6.txt") as file:
    ds = file.read()

for i in range(0, len(ds)):
    if len(set(ds[i:i+4])) == len(ds[i:i+4]):
        res = i + 4
        break

print(res)

# part 2

with open("C:/dev/adventofcode/6.txt") as file:
    ds = file.read()

for i in range(0, len(ds)):
    if len(set(ds[i:i+14])) == len(ds[i:i+14]):
        res = i + 14
        break

print(res)
