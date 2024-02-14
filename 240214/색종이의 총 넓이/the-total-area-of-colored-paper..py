n = int(input())
off_set = 100
result = 0
board = [
  [0]*200
  for _ in range(200)
]

for i in range(n):
  y1, x1 = map(int, input().split())
  y1 += off_set
  x1 += off_set
  for y in range(y1, y1+8):
    for x in range(x1, x1+8):
      board[y][x] = 1

for board_list in board:
  result += sum(board_list)
print(result)