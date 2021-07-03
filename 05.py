n = int(input())
if n < 4 and n > 1:
    print("NO SOLUTION")
    exit()

odds = n // 2 + n % 2 + 1
evens = n // 2 + 1
result = ""

for i in range(1, evens):
    result += str(i * 2) + " "
for i in range(1, odds):
    result += str(i * 2 - 1) + " "

print(result)
