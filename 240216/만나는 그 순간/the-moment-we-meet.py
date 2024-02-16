n, m = map(int, input().split())

move = [
  tuple(input().split())
  for _ in range(n+m)
]

a_current = 0
b_current = 0

a_arr = [0]
b_arr = [0]

for i, (direction, move_count) in enumerate(move, start=1):
  if i <= n:
    move_count = int(move_count)
    for count in range(1, move_count+1):
      if direction == "R":
        a_arr.append(a_current+count)
      else:
        a_arr.append(a_current-count)
    a_current = a_arr[-1]

  elif i > n:
    move_count = int(move_count)
    for count in range(1, move_count+1):
      if direction == "R":
        b_arr.append(b_current+count)
      else:
        b_arr.append(b_current-count)
    b_current = b_arr[-1]

result = -1

for i, (a, b) in enumerate(zip(a_arr, b_arr)):
  if i != 0 and a == b:
    result = i
    break
print(result)