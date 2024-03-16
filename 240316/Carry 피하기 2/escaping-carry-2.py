n = int(input())
numbers = [ 
  int(input())
  for _ in range(n)
]

result = 0
temp = 0

def carry_check(number_1, number_2, number_3):
  ans = number_1 + number_2 + number_3
  number_1 = list(str(number_1))
  number_2 = list(str(number_2))
  number_3 = list(str(number_3))
  max_len = max(len(number_1), len(number_2), len(number_3))
  len_list = [len(number_1), len(number_2), len(number_3)]
  number_list = [number_1, number_2, number_3]

  for i in range(3):
    add_count = max_len - len_list[i]
    for _ in range(add_count):
      number_list[i].insert(0, '0')

  for i in range(max_len):
    number = int(number_1[-1]) + int(number_2[-1]) + int(number_3[-1])
    if number > 9:
      return -1
    else:
      number_1.pop()
      number_2.pop()
      number_3.pop()

  return ans

for i in range(n):
  for j in range(i+1, n):
    for k in range(j+1, n):
      temp = carry_check(numbers[i], numbers[j], numbers[k])
      if temp == -1 and result == 0:
        result = -1
      else:
        result = max(result, temp)

print(result)