orders = input()

y = 0
x = 0
current_direction = 0
result = -1
time = 0

dys = [-1, 0, 1, 0]
dxs = [0, 1, 0, -1]


for order in orders:
  if order == "F":
    y = y + dys[current_direction]
    x = x + dxs[current_direction]
    time += 1

  elif order == "R":
    current_direction = (current_direction+1)%4
    time += 1

  elif order == "L":
    current_direction = (current_direction-1+4)%4
    time += 1

  if y == 0 and x == 0:
    result = time
    break

print(result)