n, time = map(int, input().split())
y, x, direction = input().split()

y = int(y)-1
x = int(x)-1

board = [ 
  [0]*n
  for _ in range(n)
]

dys = [0, -1, 1, 0]
dxs = [1, 0, 0, -1]

direction_map = {
  "R": 0,
  "D": 1,
  "U": 2,
  "L": 3
}

reverse_direction_map = {
  "0": "R",
  "1": "D",
  "2": "U",
  "3": "L"
}

def check(y, x):
  return y >= 0 and x >= 0 and y < n and x < n

while True:
  if time == 0:
    break
  ny = y + dys[direction_map[direction]]
  nx = x + dxs[direction_map[direction]]
  if check(ny, nx):
    time -= 1
    y = ny
    x = nx
  else:
    time -= 1
    direction = 3 - direction_map[direction]
    direction = reverse_direction_map[str(direction)]

print(y+1, x+1)