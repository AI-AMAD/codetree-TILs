row, col = map(int, input().split())

board = [
  [0]*col
  for _ in range(row)
]

direction = 0
y = 0
x = 0
dys = [0, 1, 0, -1]
dxs = [1, 0, -1, 0]

board[y][x] = 1

def valid(y, x):
  return y>=0 and x>=0 and y<row and x<col

for count in range(2, row*col+1):
  ny = y + dys[direction]
  nx = x + dxs[direction]
  if valid(ny, nx) and board[ny][nx] == 0:
    y = ny
    x = nx
    board[y][x] = count
  else:
    direction = (direction+1)%4
    ny = y + dys[direction]
    nx = x + dxs[direction]
    if valid(ny, nx) and board[ny][nx] == 0:
      y = ny
      x = nx
      board[y][x] = count

for i in range(row):
  for j in range(col):
    print(board[i][j], end=' ')
  print()