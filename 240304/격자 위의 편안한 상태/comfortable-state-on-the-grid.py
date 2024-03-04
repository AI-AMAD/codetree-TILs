n, m = map(int, input().split())

board = [ 
  [0]*n
  for _ in range(n)
]

informations = [
  tuple(map(int, input().split()))
  for _ in range(m)
]

dys = [-1, 1, 0, 0]
dxs = [0, 0, 1, -1]

def check(y, x):
  result = 0
  for dy, dx in zip(dys, dxs):
    ny = y + dy
    nx = x + dx
    if not ny >= 0 or not nx >= 0 or not ny < n or not nx < n:
      continue
    if board[ny][nx] == 1:
      result += 1

  if result == 3:
    return True
  else:
    return False

for information in informations:
  y, x = information
  y -= 1
  x -= 1
  board[y][x] = 1
  if check(y, x):
    print(1)
  else:
    print(0)