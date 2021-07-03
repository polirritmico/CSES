n = int(input())

while True:
    print(str(n), end = " ")
    if n == 1:
        break
    n = n // 2 if n % 2 == 0 else n * 3 + 1
