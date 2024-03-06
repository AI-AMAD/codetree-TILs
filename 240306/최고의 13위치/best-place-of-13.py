n = int(input())
board = [
  list(map(int, input().split()))
  for _ in range(n)
]

result = 0
def gold_check(y, x):
  gold = board[y][x]+board[y][x+1]+board[y][x+2]
  return gold

for y in range(n):
  for x in range(n-2):
    temp = gold_check(y, x)
    result = max(result, temp)

print(result)