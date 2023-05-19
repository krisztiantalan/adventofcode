with open("C:/dev/adventofcode/5.txt") as file:
    cargo = file.read().splitlines()

stacks = {}
for i in range(1, 10):
    stacks['stack_%i' % i] = []

for line in cargo:
    if '[' in line:
        # index 1 - column 1, index 5 - column 2, index 9 - column 3, index 13 - column 4
        # index 17 - column 5, index 21 - column 6
        # index 25 - column 7, index 29 - column 8, index 33 - column 9
        for i in range(0, len(line)):
            if line[i].isalpha():
                if i == 1:
                    stacks['stack_1'].insert(0, line[i])
                elif i == 5:
                    stacks['stack_2'].insert(0, line[i])
                elif i == 9:
                    stacks['stack_3'].insert(0, line[i])
                elif i == 13:
                    stacks['stack_4'].insert(0, line[i])
                elif i == 17:
                    stacks['stack_5'].insert(0, line[i])
                elif i == 21:
                    stacks['stack_6'].insert(0, line[i])
                elif i == 25:
                    stacks['stack_7'].insert(0, line[i])
                elif i == 29:
                    stacks['stack_8'].insert(0, line[i])
                elif i == 33:
                    stacks['stack_9'].insert(0, line[i])
    elif 'move' in line:
        line_order = [int(char) for char in line.split(' ') if char.isnumeric()]
        for i in range(0, line_order[0]):
            stacks['stack_%i' % line_order[2]].append(stacks['stack_%i' % line_order[1]][-1])
            stacks['stack_%i' % line_order[1]].pop()

res = ''.join([stacks[letter][-1] for letter in stacks])
print(res)

# part 2

with open("C:/dev/adventofcode/5.txt") as file:
    cargo = file.read().splitlines()

stacks = {}
for i in range(1, 10):
    stacks['stack_%i' % i] = []

for line in cargo:
    if '[' in line:
        for i in range(0, len(line)):
            if line[i].isalpha():
                if i == 1:
                    stacks['stack_1'].insert(0, line[i])
                elif i == 5:
                    stacks['stack_2'].insert(0, line[i])
                elif i == 9:
                    stacks['stack_3'].insert(0, line[i])
                elif i == 13:
                    stacks['stack_4'].insert(0, line[i])
                elif i == 17:
                    stacks['stack_5'].insert(0, line[i])
                elif i == 21:
                    stacks['stack_6'].insert(0, line[i])
                elif i == 25:
                    stacks['stack_7'].insert(0, line[i])
                elif i == 29:
                    stacks['stack_8'].insert(0, line[i])
                elif i == 33:
                    stacks['stack_9'].insert(0, line[i])
    elif 'move' in line:
        line_order = [int(char) for char in line.split(' ') if char.isnumeric()]
        stacks['stack_%i' % line_order[2]].extend(stacks['stack_%i' % line_order[1]][-abs(line_order[0]):])
        del stacks['stack_%i' % line_order[1]][len(stacks['stack_%i' % line_order[1]]) - line_order[0]:]

res = ''.join([stacks[letter][-1] for letter in stacks])
print(res)
