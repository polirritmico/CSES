n = input()
expected = sum(int(i) for i in range(int(n) + 1))

input_str = input()
sum_all = sum(int(i) for i in input_str.split(" "))

print(expected - sum_all)
