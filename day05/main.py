with open("input.txt") as inp:
    i = inp.read()


def find_marker(marker_length: int):
    marker = [x for x in range(marker_length)]

    pos = 0
    for cnt, char in enumerate(i):
        marker.append(char)
        marker.pop(0)

        # print(cnt, char, marker, list(set(marker)))
        if len(set(marker)) == marker_length and cnt > marker_length:
            pos = cnt + 1
            break

    return pos

# part 1
print(find_marker(4))

# part 2
print(find_marker(14))
