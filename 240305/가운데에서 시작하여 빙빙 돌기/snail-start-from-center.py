n = int(input())
end = n*n+1
board = [ 
  [0]*n
  for _ in range(n)
]

center = n // 2
y = center
x = center

dys = [1, 0, -1, 0]
dxs = [0, 1, 0, -1]
current_direction = 0

board[y][x] = 1

def in_range(y, x):
  return y>=0 and x>=0 and y<n and x<n


for number in range(2, end):
  changed_direction = (current_direction+1)%4
  ny = y + dys[changed_direction]
  nx = x + dxs[changed_direction]
  if in_range(ny, nx) and board[ny][nx] == 0:
    board[ny][nx] = number
    y = ny
    x = nx
    current_direction = changed_direction
  else:
    y = y + dys[current_direction]
    x = x + dxs[current_direction]
    board[y][x] = number

for y in range(n):
  for x in range(n):
    print(board[y][x], end=' ')
  print()