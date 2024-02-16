n, m = map(int, input().split())
information = [
  tuple(map(int, input().split()))
  for _ in range(n+m)
]

a_arr = []
b_arr = []

winner = None
temp = None
a_current = 0
b_current = 0
result = 0

def winner_changed_check(a, b):
  global winner
  global temp
  if a > b:
    temp = "a"
    if winner == temp:
      return False
    else:
      winner = temp
      return True
  elif a < b:
    temp = "b"
    if winner == temp:
      return False
    else:
      winner = temp
      return True
  elif a == b:
    return False

for i, (speed, time) in enumerate(information):
  if i < n:
    for _ in range(time):
      a_current += speed
      a_arr.append(a_current)
  else:
    for _ in range(time):
      b_current += speed
      b_arr.append(b_current)

for a, b in zip(a_arr, b_arr):
  if winner_changed_check(a, b):
    result += 1

if result == 0:
  print(result)
else:
  print(result-1)