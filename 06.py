t = int(input())
to_check = []
for i in range(t):
    to_check.append(tuple(int(i) for i in input().split(" ")))

for coords in to_check:
    row = coords[0]
    col = coords[1]

    if row >= col:
        is_even = True if row % 2 == 0 else False
        incremental = False if is_even else True
        if incremental:
            value = (row - 1) * (row - 1) + 1
            value += col - 1
        else:
            value = row * row
            value -= col - 1
    else:
        is_even = True if col % 2 == 0 else False
        incremental = True if is_even else False
        if incremental:
            value = (col - 1) * (col - 1) + 1
            value += row - 1
        else:
            value = col * col
            value -= row - 1

    print(value)