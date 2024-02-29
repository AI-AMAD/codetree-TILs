n = int(input())

informations = [
  tuple(input().split())
  for _ in range(n)
]

dy = [0, -1, 0, 1]
dx = [-1, 0, 1, 0]

current_location = [0, 0]

for information in informations:
  direct, distance = information[0], information[1]
  distance = int(distance)
  if direct == "W":
    for _ in range(distance):
      current_location[0] = current_location[0] + dy[0]
      current_location[1] = current_location[1] + dx[0]
  elif direct == "S":
    for _ in range(distance):
      current_location[0] = current_location[0] + dy[1]
      current_location[1] = current_location[1] + dx[1]
  elif direct == "E":
    for _ in range(distance):
      current_location[0] = current_location[0] + dy[2]
      current_location[1] = current_location[1] + dx[2]
  elif direct == "N":
    for _ in range(distance):
      current_location[0] = current_location[0] + dy[3]
      current_location[1] = current_location[1] + dx[3]

y, x = current_location[0], current_location[1]
print(x, y)