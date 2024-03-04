n = int(input())
end = n*4+1
board = [ 
  list(input())
  for _ in range(n)
]

start = int(input())

information_map = {
  "1": {
    "y": 0,
    "x": 0,
    "laser_direction": "D"
  }
}
y = 0
x = 0
temp_dys = [0, 1, 0, -1]
temp_dxs = [1, 0, -1, 0]
temp_current_direction = 0
mapper = {
  "0": "D",
  "1": "L",
  "2": "U",
  "3": "R",
}

def in_range(y, x):
  return y>=0 and x>=0 and y<n and x<n

for start_number in range(2, end):
  ny = y + temp_dys[temp_current_direction]
  nx = x + temp_dxs[temp_current_direction]
  if in_range(ny, nx):
    y = ny
    x = nx
    information_map[str(start_number)] = {"y": y, "x": x, "laser_direction": mapper[str(temp_current_direction)]}
  else:
    temp_current_direction = (temp_current_direction+1)%4
    information_map[str(start_number)] = {"y": y, "x": x, "laser_direction": mapper[str(temp_current_direction)]}



    #  D  L   U  R
dys = [1, 0, -1, 0]
dxs = [0, -1, 0, 1]
result = 1

real_mapper = {
  "D": 0,
  "L": 1,
  "U": 2,
  "R": 3,
}

location_y = information_map[str(start)]["y"]
location_x = information_map[str(start)]["x"]
laser = information_map[str(start)]["laser_direction"]

def next_laser(current_laser, mirror):
  if current_laser == "D" and mirror == "\\":
    return "R"
  elif current_laser == "D" and mirror == "/":
    return "L"
  elif current_laser == "L" and mirror == "\\":
    return "U"
  elif current_laser == "L" and mirror == "/":
    return "D"
  elif current_laser == "U" and mirror == "\\":
    return "L"
  elif current_laser == "U" and mirror == "/":
    return "R"
  elif current_laser == "R" and mirror == "\\":
    return "D"
  elif current_laser == "R" and mirror == "/":
    return "U"

while True:
  mirror = board[location_y][location_x]
  laser = next_laser(laser, mirror)
  next_y = location_y + dys[real_mapper[laser]]
  next_x = location_x + dxs[real_mapper[laser]]
  
  if not in_range(next_y, next_x):
    break

  result += 1
  location_y = next_y
  location_x = next_x

print(result)