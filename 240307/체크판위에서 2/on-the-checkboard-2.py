row, col = map(int, input().split())
board = [ 
  list(input().split())
  for _ in range(row)
]
# 점프시 현재 타일의 색깔과 점프 마친 후 타일의 색깔은 달라야 한다 ex) W -> B,  B -> W
# 점프시 현재 타일보다 항상 1칸 이상은 오른쪽에 위치해야 하며 동시에 1칸 이상 아래쪽으로만 가능
# 바꿔 말하면 점프시 y축은 항상 y+1 되고 x축도 항상 x+1 되는 곳으로만 이동 가능
# 시작, 도착 지점을 제외하고 점프는 2번만 가능

result = 0
start_color = board[0][0]
start_y = 0
start_x = 0

for y in range(row):
  for x in range(col):
    if board[y][x] != start_color and y>start_y and x>start_x:
      second_y = y
      second_x = x
      second_color = board[second_y][second_x]
      for y_2 in range(second_y, row):
        for x_2 in range(second_x, col):
          if board[y_2][x_2] != second_color and y_2>second_y and x_2>second_x:
            third_y = y_2
            third_x = x_2
            third_color = board[third_y][third_x]
            for y_3 in range(third_y, row):
              for x_3 in range(third_x, col):
                if board[y_3][x_3] != third_color and y_3>third_y and x_3>third_x and y_3 == row-1 and x_3 == col-1:
                  result += 1

print(result)