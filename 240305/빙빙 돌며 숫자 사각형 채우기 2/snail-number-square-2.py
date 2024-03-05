row, col = map(int, input().split())
end = row*col+1
board = [ 
  [0]*col
  for _ in range(row)
]

dys = [1, 0, -1, 0]
dxs = [0, 1, 0, -1]
current_direction = 0
y = 0
x = 0

board[0][0] = 1

def in_range(y, x):
  return y>=0 and x>=0 and y<row and x<col

for number in range(2, end):
  ny = y + dys[current_direction]
  nx = x + dxs[current_direction]
  if in_range(ny, nx) and board[ny][nx] == 0:
    board[ny][nx] = number
    y = ny
    x = nx
  else:
    current_direction = (current_direction+1)%4
    ny = y + dys[current_direction]
    nx = x + dxs[current_direction]
    board[ny][nx] = number
    y = ny
    x = nx

for y in range(row):
  for x in range(col):
    print(board[y][x], end=' ')
  print()