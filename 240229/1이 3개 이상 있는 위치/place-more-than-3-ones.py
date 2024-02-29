n = int(input())
board = [ 
  list(map(int, input().split()))
  for _ in range(n)
]

dys = [1, -1, 0, 0]
dxs = [0, 0, -1, 1]
result = 0

def range_check(y, x):
  return y >= 0 and x >= 0 and y < n and x < n

for y in range(n):
  for x in range(n):
    count_1 = 0
    for dy, dx in zip(dys, dxs):
      ny = y + dy
      nx = x + dx
      if range_check(ny, nx) and board[ny][nx] == 1:
        count_1 += 1
    if count_1 >= 3:
      result += 1

print(result)