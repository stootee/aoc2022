with open('input.txt') as inp:
    i = inp.read()

# i = """$ cd /
# $ ls
# dir a
# 14848514 b.txt
# 8504156 c.dat
# dir d
# $ cd a
# $ ls
# dir e
# 29116 f
# 2557 g
# 62596 h.lst
# $ cd e
# $ ls
# 584 i
# $ cd ..
# $ cd ..
# $ cd d
# $ ls
# 4060174 j
# 8033020 d.log
# 5626152 d.ext
# 7214296 k"""

DIRECTORY_TREE = {'/': {'parent_directory': '', 'contents': []}}
SMALL_DIRECTORIES = []

parent_directory = ''
current_directory = ''
for line in i.splitlines():
    line_items = line.split(' ')
    if line_items[0] == '$':
        # this is a user input
        if line_items[1] == 'cd':
            # this is a change of directory
            if line_items[2] == '..':
                current_directory = parent_directory

            else:
                parent_directory = current_directory
                current_directory = line_items[2]

            if current_directory in DIRECTORY_TREE.keys():
                pass
            else:
                DIRECTORY_TREE[current_directory] = {'parent_directory': parent_directory, 'contents': []}

    else:
        if line_items[0] == 'dir':
            # this is a directory in the current directory
            DIRECTORY_TREE[current_directory]['contents'].append({'name': line_items[1], 'size': '0', 'type': 'dir'})
        elif line_items[0].isnumeric():
            DIRECTORY_TREE[current_directory]['contents'].append({'name': line_items[1], 'size': int(line_items[0]), 'type': 'file'})


def get_dir_size(directory_name: str, directory_contents: list):
    _directory_size = 0
    _cnt = 0
    for _y in directory_contents:
    # while _directory_size <= 100000 and _cnt < len(directory_contents):
    #     _y = directory_contents[_cnt]
        print('y', _y)
        if _y['type'] == 'dir':
            _directory_size += get_dir_size(_y['name'], DIRECTORY_TREE[_y['name']]['contents'])
        else:
            _directory_size += _y['size']

        _cnt += 1

    if _directory_size <= 100000:
        SMALL_DIRECTORIES.append((directory_name, _directory_size))

    return _directory_size


print(DIRECTORY_TREE['/'])
# for directory, info in DIRECTORY_TREE.items():
directory_size = 0
directory_size += get_dir_size('/', DIRECTORY_TREE['/']['contents'])


print(SMALL_DIRECTORIES)



