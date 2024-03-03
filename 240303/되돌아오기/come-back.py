n = int(input())

board = [ 
  [0]*2000
  for _ in range(2000)
]

y = 1000
x = 1000
time = 0

informations = [
  tuple(input().split())
  for _ in range(n)
]

board[y][x] = "start"

dys = [-1, 1, 0, 0]
dxs = [0, 0, 1, -1]

mapper = {
  "N": 0,
  "S": 1,
  "E": 2,
  "W": 3
}

ancor = False

for information in informations:
  direction, distance = information
  distance = int(distance)
  if ancor:
    break
  for _ in range(distance):
    ny = y + dys[mapper[direction]]
    nx = x + dxs[mapper[direction]]
    time += 1
    if board[ny][nx] == "start":
      ancor = True
      break
    else:
      y = ny
      x = nx

if ancor:
  print(time)
else:
  print(-1)