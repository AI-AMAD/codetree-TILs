m, n = map(int, input().split())

information = [
  tuple(map(int, input().split()))
  for _ in range(m+n)
]

a_arr = []
b_arr = []

a_current = 0
b_current = 0

for i, (speed, time) in enumerate(information, start=1):
  if i <= m:
    for _ in range(time):
      a_current += speed
      a_arr.append(a_current)
  else:
    for _ in range(time):
      b_current += speed
      b_arr.append(b_current)

a = "a"
b = "b"
ab = "ab"
present_victory = None
result = 0

for a_man, b_man in zip(a_arr, b_arr):
  if a_man > b_man:
    if present_victory != a:
      present_victory = a
      result += 1
  elif b_man > a_man:
    if present_victory != b:
      present_victory = b
      result += 1
  elif a_man == b_man:
    if present_victory != ab:
      present_victory = ab
      result += 1

print(result)