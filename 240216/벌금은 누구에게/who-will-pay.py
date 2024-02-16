student, count, target = map(int, input().split())

students = [0] * (student+1)
first_student = -1

for i in range(count):
  which_student = int(input())
  students[which_student] += 1
  if students[which_student] == target:
    first_student = which_student
    break

print(first_student)