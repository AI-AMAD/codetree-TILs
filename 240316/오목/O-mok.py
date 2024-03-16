board = [ 
  list(map(int, input().split()))
  for _ in range(19)
]

result = []
flag = False

def in_range_garo(i, j):
  return i<15

def in_range_sero_and_dialogue_up(i, j):
  return j<15

def in_range_dialogue_down(i, j):
  return i<15 and j<15

def garo_check(i, j):
  if in_range_garo(i, j):
    if board[i][j] == board[i][j+1] == board[i][j+2] == board[i][j+3] == board[i][j+4]:
      return True
    else:
      return False
  else:
    return False

def sero_check(i, j):
  if in_range_sero_and_dialogue_up(i, j):
    if board[i][j] == board[i+1][j] == board[i+2][j] == board[i+3][j] == board[i+4][j]:
      return True
    else:
      return False
  else: 
    return False

def dialogue_check_down(i, j):
  if in_range_dialogue_down(i, j):
    if board[i][j] == board[i+1][j+1] == board[i+2][j+2] == board[i+3][j+3] == board[i+4][j+4]:
      return True
    else:
      return False
  else:
    return False

def dialogue_check_up(i, j):
  if in_range_sero_and_dialogue_up(i, j):
    if board[i][j] == board[i-1][j+1] == board[i-2][j+2] == board[i-3][j+3] == board[i-4][j+4]:
      return True
    else:
      return False
  else:
    return False

def check(i, j):
  if board[i][j] == 1: 
    if garo_check(i, j):
      result.append(board[i][j])
      result.append(i+1)
      result.append(j+3)
      return result
    elif sero_check(i, j):
      result.append(board[i][j])
      result.append(i+3)
      result.append(j+1)
      return result
    elif dialogue_check_down(i, j):
      result.append(board[i][j])
      result.append(i+3)
      result.append(j+3)
      return result
    elif dialogue_check_up(i, j):
      result.append(board[i][j])
      result.append(i-1)
      result.append(j+3)
      return result
  elif board[i][j] == 2:
    if garo_check(i, j):
      result.append(board[i][j])
      result.append(i+1)
      result.append(j+3)
      return result
    elif sero_check(i, j):
      result.append(board[i][j])
      result.append(i+3)
      result.append(j+1)
      return result
    elif dialogue_check_down(i, j):
      result.append(board[i][j])
      result.append(i+3)
      result.append(j+3)
      return result
    elif dialogue_check_up(i, j):
      result.append(board[i][j])
      result.append(i-1)
      result.append(j+3)
      return result

  return result

for i in range(19):
  if flag == True:
    break
  for j in range(19):
    number = board[i][j]
    if number == 0:
      continue
    if check(i, j):
      flag = True
      break

print(result[0])
print(result[1], result[2])