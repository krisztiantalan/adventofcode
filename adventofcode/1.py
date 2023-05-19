txt = open("C:/dev/adventofcode/1.txt")
inventory = txt.read()
txt.close()

result = [0]

for num in inventory.split('\n'):
    if result[0] == 0:
        counter = 0
    try:
        try:
            result[counter] += int(num)
        except IndexError:
            result.append(int(num))
    except ValueError:
        counter += 1

result.sort()
print(result[-1] + result[-2] + result[-3])
