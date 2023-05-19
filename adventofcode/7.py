with open("C:/dev/adventofcode/7.txt") as file:
    cmds = file.read().splitlines()

with open('C:/dev/adventofcode/7_test.txt') as testfile:
    testcmds = testfile.read().splitlines()

dir_tree = {}


def get_parent_dir(value, dirs):
    # value is current_dir
    # dirs is dir_tree
    for entry in dirs:
        if isinstance(dirs[entry], dict):
            if value in dirs[entry].values():
                if dirs[entry]:
                    return dirs[entry]
                else:
                    return dir_tree['/']
            else:
                if get_parent_dir(value, dirs[entry]):
                    return get_parent_dir(value, dirs[entry])


def count_directory_sizes(dirs):
    # start from dir_tree['/']
    for entry in dirs:
        if isinstance(dirs[entry], dict):
            dirs['size'] += dirs[entry]['size']
            count_directory_sizes(dirs[entry])


def count_max100kdirs_size(dirs):
    maxdirsize = 0
    for entry in dirs:
        if isinstance(dirs[entry], dict):
            if dirs[entry]['size'] <= 100000:
                maxdirsize += dirs[entry]['size']
            maxdirsize += count_max100kdirs_size(dirs[entry])
    return maxdirsize


for cmd in cmds:

    cmd = cmd.split(' ')

    if cmd[0] == '$':
        if cmd[1] == 'cd':
            if cmd[2] == '/':
                dir_tree['/'] = {
                    'size': 0,
                }
                current_dir = dir_tree['/']
            elif cmd[2] == '..':
                current_dir = get_parent_dir(current_dir, dir_tree)
            else:
                current_dir = current_dir['dir %s' % cmd[2]]
        elif cmd[1] == 'ls':
            pass
    elif cmd[0] == 'dir':
        current_dir['dir %s' % cmd[1]] = {
            'size': 0,
        }
    elif cmd[0].isnumeric():
        current_dir[cmd[1]] = int(cmd[0])
        current_dir['size'] += int(cmd[0])

count_directory_sizes(dir_tree['/'])
print(count_max100kdirs_size(dir_tree))
