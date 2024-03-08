target = list(input())
end = len(target)
result = 0

def change_to_decimal(number_list):
  binary_number_list = ['0','b']
  binary_number_list.extend(number_list)
  binary_number = ''.join(binary_number_list)
  decimal = int(binary_number, 2)
  return decimal

for i in range(1, end):
  if target[i] == '0':
    target[i] = '1'
    temp = change_to_decimal(target)
    result = max(temp, result)
    target[i] = '0'
  elif target[i] == '1':
    target[i] = '0'
    temp = change_to_decimal(target)
    result = max(temp, result)
    target[i] = '1'

print(result)