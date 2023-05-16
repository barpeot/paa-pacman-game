# 0 = empty black rectangle, 0 = dot, 0 = big dot, 3 = vertical line,
# 4 = horizontal line, 5 = top right, 6 = top left, 7 = bot left, 8 = bot right
# 9 = gate
boards = [
[6, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5],
[3, 6, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 6, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 3],
[3, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 3, 3],
[3, 3, 0, 6, 4, 4, 5, 0, 6, 4, 4, 4, 5, 0, 3, 3, 0, 6, 4, 4, 4, 5, 0, 6, 4, 4, 5, 0, 3, 3],
[3, 3, 0, 3, 0, 0, 3, 0, 3, 0, 0, 0, 3, 0, 3, 3, 0, 3, 0, 0, 0, 3, 0, 3, 0, 0, 3, 0, 3, 3],
[3, 3, 0, 7, 4, 4, 8, 0, 7, 4, 4, 4, 8, 0, 7, 8, 0, 7, 4, 4, 4, 8, 0, 7, 4, 4, 8, 0, 3, 3],
[3, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 3],
[3, 3, 0, 6, 4, 4, 5, 0, 6, 5, 0, 6, 4, 4, 4, 4, 4, 4, 5, 0, 6, 5, 0, 6, 4, 4, 5, 0, 3, 3],
[3, 3, 0, 7, 4, 4, 8, 0, 3, 3, 0, 7, 4, 4, 5, 6, 4, 4, 8, 0, 3, 3, 0, 7, 4, 4, 8, 0, 3, 3],
[3, 3, 0, 0, 0, 0, 0, 0, 3, 3, 0, 0, 0, 0, 3, 3, 0, 0, 0, 0, 3, 3, 0, 0, 0, 0, 0, 0, 3, 3],
[3, 7, 4, 4, 4, 4, 5, 0, 3, 7, 4, 4, 5, 0, 3, 3, 0, 6, 4, 4, 8, 3, 0, 6, 4, 4, 4, 4, 8, 3],
[3, 0, 0, 0, 0, 0, 3, 0, 3, 6, 4, 4, 8, 0, 7, 8, 0, 7, 4, 4, 5, 3, 0, 3, 0, 0, 0, 0, 0, 3],
[3, 0, 0, 0, 0, 0, 3, 0, 3, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 3, 0, 3, 0, 0, 0, 0, 0, 3],
[8, 0, 0, 0, 0, 0, 3, 0, 3, 3, 0, 6, 4, 4, 9, 9, 4, 4, 5, 0, 3, 3, 0, 3, 0, 0, 0, 0, 0, 7],
[4, 4, 4, 4, 4, 4, 8, 0, 7, 8, 0, 3, 0, 0, 0, 0, 0, 0, 3, 0, 7, 8, 0, 7, 4, 4, 4, 4, 4, 4],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 2, 2, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[4, 4, 4, 4, 4, 4, 5, 0, 6, 5, 0, 3, 0, 0, 0, 0, 0, 0, 3, 0, 6, 5, 0, 6, 4, 4, 4, 4, 4, 4],
[5, 0, 0, 0, 0, 0, 3, 0, 3, 3, 0, 7, 4, 4, 4, 4, 4, 4, 8, 0, 3, 3, 0, 3, 0, 0, 0, 0, 0, 6],
[3, 0, 0, 0, 0, 0, 3, 0, 3, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 3, 0, 3, 0, 0, 0, 0, 0, 3],
[3, 0, 0, 0, 0, 0, 3, 0, 3, 3, 0, 6, 4, 4, 4, 4, 4, 4, 5, 0, 3, 3, 0, 3, 0, 0, 0, 0, 0, 3],
[3, 6, 4, 4, 4, 4, 8, 0, 7, 8, 0, 7, 4, 4, 5, 6, 4, 4, 8, 0, 7, 8, 0, 7, 4, 4, 4, 4, 5, 3],
[3, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 3],
[3, 3, 0, 6, 4, 4, 5, 0, 6, 4, 4, 4, 5, 0, 3, 3, 0, 6, 4, 4, 4, 5, 0, 6, 4, 4, 5, 0, 3, 3],
[3, 3, 0, 7, 4, 5, 3, 0, 7, 4, 4, 4, 8, 0, 7, 8, 0, 7, 4, 4, 4, 8, 0, 3, 6, 4, 8, 0, 3, 3],
[3, 3, 0, 0, 0, 3, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 3, 0, 0, 0, 3, 3],
[3, 7, 4, 5, 0, 3, 3, 0, 6, 5, 0, 6, 4, 4, 4, 4, 4, 4, 5, 0, 6, 5, 0, 3, 3, 0, 6, 4, 8, 3],
[3, 6, 4, 8, 0, 7, 8, 0, 3, 3, 0, 7, 4, 4, 5, 6, 4, 4, 8, 0, 3, 3, 0, 7, 8, 0, 7, 4, 5, 3],
[3, 3, 0, 0, 0, 0, 0, 0, 3, 3, 0, 0, 0, 0, 3, 3, 0, 0, 0, 0, 3, 3, 0, 0, 0, 0, 0, 0, 3, 3],
[3, 3, 0, 6, 4, 4, 4, 4, 8, 7, 4, 4, 5, 0, 3, 3, 0, 6, 4, 4, 8, 7, 4, 4, 4, 4, 5, 0, 3, 3],
[3, 3, 0, 7, 4, 4, 4, 4, 4, 4, 4, 4, 8, 0, 7, 8, 0, 7, 4, 4, 4, 4, 4, 4, 4, 4, 8, 0, 3, 3],
[3, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 3],
[3, 7, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 8, 3],
[7, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 8]
]
