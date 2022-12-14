with open('input.txt') as inp:
    i = inp.read()

# i = """30373
# 25512
# 65332
# 33549
# 35390"""

grid = []
row_count = 0
columns = []
column_count = 0
for row in i.splitlines():
    grid.append([int(tree) for tree in list(row)])
    column_count = 0
    for tree in row:
        if row_count == 0:
            # columns.append([int(tree) for tree in list(row)])
            columns.append([int(tree)])
        else:
            columns[column_count].append(int(tree))

        column_count += 1

    row_count += 1

visible = []
for x in range(row_count):
    for y in range(column_count):

        is_visible = False

        if x == 0 or y == 0 or x == row_count - 1 or y == column_count - 1:
            is_visible = True
            visible.append((x, y))

        if not is_visible:

            tree = grid[x][y]
            left_this_row = grid[x][:y]
            right_this_row = grid[x][y - len(grid[x]) + 1:]
            top_this_column = columns[y][:x]
            bottom_this_column = columns[y][x - len(grid[y]) + 1:]

            # print(x, y)
            # print(tree)
            # print(grid[x])
            # print(left_this_row)
            # print(right_this_row)
            # print(columns[y])
            # print(top_this_column)
            # print(bottom_this_column)

            if tree > max(left_this_row):
                is_visible = True
                # print(1)

            elif tree > max(right_this_row):
                is_visible = True
                # print(2)

            elif tree > max(top_this_column):
                is_visible = True
                # print(3)

            elif tree > max(bottom_this_column):
                is_visible = True
                # print(4)

            if is_visible:
                visible.append((x, y))

# part 1
print(visible)
print(len(visible))


def calculate_score(tree, our_list):
    blocked = False
    this_score = 0

    # print(our_list)

    if our_list:
        while this_score < len(our_list) and not blocked:
            z = our_list[this_score]
            # print(z)
            this_score += 1
            if tree <= z:
                blocked = True

    return this_score


high_score = 0
for x in range(row_count):
    for y in range(column_count):

        is_visible = False

        if x == 0 or y == 0 or x == row_count - 1 or y == column_count - 1:
            is_visible = True

        if not is_visible:
            tree = grid[x][y]
            left_this_row = grid[x][:y]
            right_this_row = grid[x][y - len(grid[x]) + 1:]
            top_this_column = columns[y][:x]
            bottom_this_column = columns[y][x - len(grid[y]) + 1:]

            score = 0
            # print(x, y, "(", tree, ")")

            this_score_a = calculate_score(tree, list(reversed(left_this_row)))

            this_score_b = calculate_score(tree, right_this_row)

            this_score_c = calculate_score(tree, list(reversed(top_this_column)))

            this_score_d = calculate_score(tree, bottom_this_column)

            this_score = this_score_a * this_score_b * this_score_c * this_score_d
            # print(this_score)
            if this_score > high_score:
                high_score = this_score

print(high_score)


