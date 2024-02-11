n = int(input())
numbers = [i for i in map(int, input().split())]
print(numbers.sort())
print(numbers.sort(reverse=True))