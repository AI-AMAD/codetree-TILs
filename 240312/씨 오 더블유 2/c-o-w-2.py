n = int(input())
string = input()
result = 0

for i in range(n):
  if string[i] == "C":
    for j in range(i, n):
      if string[j] == "O":
        for k in range(j, n):
          if string[k] == "W":
            result += 1

print(result)