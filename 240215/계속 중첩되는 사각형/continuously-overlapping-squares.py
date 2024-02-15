n = int(input())
rect = [
  tuple(map(int,input().split()))
  for _ in range(n)
]
board = [
  [0]*201
  for _ in range(201)
]
off_set = 100
color = None

for i, (y1, x1, y2, x2) in enumerate(rect, start=1):
  if i%2 == 0:
    color = 1
    for y in range(y1, y2):
      for x in range(x1, x2):
        board[y][x] = color
  else:
    color = 2
    for y in range(y1, y2):
      for x in range(x1, x2):
        board[y][x] = color

blue_color = 0

for y in range(201):
  for x in range(201):
    if board[y][x] == 1:
      blue_color += 1

print(blue_color)