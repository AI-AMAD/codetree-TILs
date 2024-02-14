n = 3
board = [[0]*2000 for _ in range(2000)]
off_set = 1000

for i in range(n):
  y1, x1, y2, x2 = map(int, input().split())
  y1 += off_set
  x1 += off_set
  y2 += off_set
  x2 += off_set
  for y in range(y1, y2):
    for x in range(x1, x2):
      if i == 0 or i == 1:
        board[y][x] = 1
      else:
        board[y][x] = 2

result = 0
for board_list in board:
  for count in board_list:
    if count == 1:
      result += 1
print(result)