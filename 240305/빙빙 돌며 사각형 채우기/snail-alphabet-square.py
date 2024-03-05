row, col = map(int, input().split())
end = row*col+1
board = [ 
  [0]*col
  for _ in range(row)
]

y = 0
x = 0
ascii_code = 65
current_direction = 0

dys = [0, 1, 0, -1]
dxs = [1, 0, -1, 0]

board[y][x] = chr(ascii_code)

def in_range(y, x):
  return y>=0 and x>=0 and y<row and x<col

def next_ascii_code(current_ascii_code):
  global ascii_code
  if current_ascii_code != 90:
    current_ascii_code += 1
    ascii_code = current_ascii_code
    return ascii_code
  else:
    current_ascii_code = 65
    ascii_code = current_ascii_code
    return ascii_code

for i in range(2, end):
  ny = y + dys[current_direction]
  nx = x + dxs[current_direction]
  ascii_code = next_ascii_code(ascii_code)
  if not in_range(ny, nx) or board[ny][nx] != 0:
    current_direction = (current_direction+1)%4
    ny = y + dys[current_direction]
    nx = x + dxs[current_direction]
    board[ny][nx] = chr(ascii_code)
    y = ny
    x = nx
  else:
    board[ny][nx] = chr(ascii_code)
    y = ny
    x = nx

for y in range(row):
  for x in range(col):
    print(board[y][x], end=' ')
  print()