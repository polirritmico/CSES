def solve(index):
	if index < 10:
	 	return index

	cluster = 10
	pot = 0
	while cluster <= index:
		pot += 1
		add = ((10 ** pot) * 9) * (pot + 1)
		cluster += add
	cluster = cluster - add
	pot += 1

	i = (index - cluster) // pot
	number = i + 10 ** (pot - 1)
	module = (index - cluster) % pot

	return int(str(number)[module])


queries = int(input())
results = []
for query in range(queries):
	results.append(solve(int(input())))

print(*results, end="\n")
