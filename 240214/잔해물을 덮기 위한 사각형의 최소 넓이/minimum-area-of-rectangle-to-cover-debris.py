n = 2
board = [
  [0]*15
  for _ in range(15)
]
off_set = 3
first_rect_y1_x1_y2_x2=[]

def max_width(y1, x1, y2, x2):
  width_1 = 0
  width_2 = 0
  for i in range(x1, x2):
    if board[y1][i] == 1:
      width_1 += 1
  for i in range(x1, x2):
    if board[y2-1][i] == 1:
      width_2 += 1
  return max(width_1, width_2)

def max_length(y1, x1, y2, x2):
  length_1 = 0
  length_2 = 0 
  for i in range(y1, y2):
    if board[i][x1] == 1:
      length_1 += 1
  for i in range(y1, y2):
    if board[i][x2-1] == 1:
      length_2 += 1
  return max(length_1, length_2)

for i in range(n):
  y1, x1, y2, x2 = map(int, input().split())
  if i == 0:
    first_rect_y1_x1_y2_x2.append([y1, x1, y2, x2])
  y1+=off_set
  x1+=off_set
  y2+=off_set
  x2+=off_set
  for y in range(y1, y2):
    for x in range(x1, x2):
      if i == 0:
        board[y][x] = 1
      else:
        board[y][x] = 2
y1, x1, y2, x2 = first_rect_y1_x1_y2_x2[0]
y1+=off_set
x1+=off_set
y2+=off_set
x2+=off_set
width = max_width(y1, x1, y2, x2)
length = max_length(y1, x1, y2, x2)
print(width*length)