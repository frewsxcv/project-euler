with open("triangle.txt") as open_file:
    triangle_rows = [map(int, line.split()) for line in open_file]

for row_index in range(1, len(triangle_rows)):
    prev_row = triangle_rows[row_index-1]
    curr_row = triangle_rows[row_index]

    for item_index, item in enumerate(prev_row):
        # first item
        if item_index == 0:
            curr_row[item_index] = curr_row[item_index] + item

        # middle item
        if 0 < item_index <= len(prev_row) - 1:
            curr_row[item_index] = curr_row[item_index] + \
                max(item, prev_row[item_index - 1])

        # last item
        if item_index == len(prev_row) - 1:
            curr_row[item_index + 1] = curr_row[item_index + 1] + item

print max(triangle_rows[-1])
