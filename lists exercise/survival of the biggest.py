input_string = list(map(int, input().split()))
n = int(input())
for _ in range(n):
    input_string.remove(min(input_string))
print(input_string)

