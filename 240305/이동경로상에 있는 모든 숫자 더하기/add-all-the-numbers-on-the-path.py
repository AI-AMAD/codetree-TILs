n, ordercount = map(int, input().split())
orders = input()
board = [ 
  list(map(int, input().split()))
  for _ in range(n)
]
center = n//2
y = center
x = center

dys = [-1, 0, 1, 0]
dxs = [0, 1, 0, -1]
current_direction = 0

result = board[y][x]

def in_range(y, x):
  return y>=0 and x>=0 and y<n and x<n

for order in orders:
  if order == "R":
    current_direction = (current_direction+1)%4

  elif order == "L":
    current_direction = (current_direction-1+4)%4

  elif order == "F":
    ny = y + dys[current_direction]
    nx = x + dxs[current_direction]
    if in_range(ny, nx):
      result += board[ny][nx]
      y = ny
      x = nx

print(result)