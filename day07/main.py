with open('input.txt') as inp:
    i = inp.read()

directory_tree = {'/': {'parent_directory': '', 'contents': []}}

parent_directory = ''
for line in i.splitlines():
    line_items = line.split(' ')
    if line_items[0] == '$':
        # this is a user input
        if line_items[1] == 'cd':
            # this is a change of directory
            if line_items[2] == '..':
                current_directory = parent_directory

            else:
                current_directory = line_items[2]

            parent_directory = directory_tree[current_directory]


