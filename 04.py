n = int(input())
arr = [int(i) for i in input().split(" ")]

steps = 0
for i in range(1, n):
    current = arr[i]
    prev = arr[i - 1]
    if current < prev:
        steps += (prev - current)
        arr[i] = prev

print(steps)
