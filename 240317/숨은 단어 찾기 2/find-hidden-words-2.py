row, col = map(int, input().split())
board = [ 
  list(input())
  for _ in range(row)
]

result = 0
temp = 0

dys = [0, 1, 0, -1, -1, 1, 1, -1]
dxs = [1, 0, -1, 0, 1, 1, -1, -1]

def in_range(y, x):
  return y>=0 and x>=0 and y<row and x<col

for y in range(row):
  for x in range(col):
    if board[y][x] != "L":
      continue
    for dy, dx in zip(dys, dxs):
      current_y = y
      current_x = x
      temp = 0 
      for _ in range(2):
        next_y = current_y + dy
        next_x = current_x + dx
        if in_range(next_y, next_x) and board[next_y][next_x] == "E":
          current_y = next_y
          current_x = next_x
          temp += 1
          if temp == 2:
            result += 1

print(result)