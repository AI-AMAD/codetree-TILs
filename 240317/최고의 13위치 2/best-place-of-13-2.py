n = int(input())
board = [ 
  list(map(int, input().split()))
  for _ in range(n)
]
result = 0 
temp = 0

def in_range(x):
  return x<n

def gold_check(y, x):
  gold = board[y][x] + board[y][x+1] + board[y][x+2]
  return gold

def overlap_check(y_1, x_1, y_2, x_2):
  if y_1 != y_2:
    return True
  if y_1 == y_2:
    list_1 = [x_1, x_1+1, x_1+2]
    list_2 = [x_2, x_2+1, x_2+2]
    for number in list_2:
      if number in list_1:
        return False
    return True

for y_1 in range(n):
  for x_1 in range(n):
    if not in_range(x_1+2):
      continue
    gold_1 = gold_check(y_1, x_1)

    for y_2 in range(n):
      for x_2 in range(n):
        if not in_range(x_2+2):
          continue
        if not overlap_check(y_1, x_1, y_2, x_2):
          continue
        gold_2 = gold_check(y_2, x_2)

        result = max(result, gold_1+gold_2)

print(result)