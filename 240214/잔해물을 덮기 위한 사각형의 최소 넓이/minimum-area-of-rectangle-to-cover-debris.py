n = 2
board = [
  [0]*2000
  for _ in range(2000)
]
off_set = 1000
first_rect_y1_x1_y2_x2=[]

def max_width(new_board):
  max_width = 0
  for width in new_board:
    if width[0] == 1 and width[-1] == 1:
      max_width = len(width)
      return max_width
    else:
      temp = 0
      for i in width:
        if i == 1:
          temp += 1
        max_width = max(max_width, temp)
  return max_width

def change_list(list_):
  changed_list = []
  for y in range(len(list_[0])):
    shallow = []
    for x in range(len(list_)):
      shallow.append(list_[x][y])
    changed_list.append(shallow)
  return changed_list

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

new_board =[]
for y in range(y1, y2):
  shallow = []
  for x in range(x1, x2):
    shallow.append(board[y][x])
  new_board.append(shallow)

new_board_2 = change_list(new_board)

width = max_width(new_board)
length = max_width(new_board_2)

print(width*length)