n = int(input())

board = [[0]*200 for _ in range(200)]
OFF_SET = 100

for i in range(n):
  y1, x1, y2, x2 = map(int, input().split())
  y1 += OFF_SET
  x1 += OFF_SET
  y2 += OFF_SET
  x2 += OFF_SET
  for y in range(y1, y2):
    for x in range(x1, x2):
      board[y][x] = 1

result = 0
for board_list in board:
  result += sum(board_list)

print(result)