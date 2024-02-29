orders = input()

dy = []
dx = []

current_location = [0, 0]
direct = 3

dy = [0, -1, 0, 1]
dx = [1, 0, -1, 0]

def change_direction_R(current_direction):
  direct = (current_direction+1)%4
  return direct

def change_direction_L(current_direction):
  direct = (current_direction-1+4)%4
  return direct

for order in orders:
  if order == "L":
    direct = change_direction_L(direct)
  elif order == "R":
    direct = change_direction_R(direct)
  elif order == "F":
    current_location[0] += dy[direct]
    current_location[1] += dx[direct]

y = current_location[0] 
x = current_location[1] 

print(x, y)