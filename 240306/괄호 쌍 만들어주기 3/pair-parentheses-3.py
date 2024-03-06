letters = list(input())
result = 0

for index_1, letter_1 in enumerate(letters):
  if letter_1 == ")":
    continue
  for index_2, letter_2 in enumerate(letters):
    if index_2 <= index_1:
      continue
    if letter_2 == ")":
      result += 1

print(result)