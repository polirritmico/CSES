def solve(index):
	if index < 10:
	 	return index

	cluster = 10
	pot = 0
	while True:
		pot += 1
		add = cluster + ((10 ** pot) * 9) * (pot + 1)
		if add > index:
			pot += 1
			break
		cluster = add

	i = (index - cluster) // pot
	number = i + 10 ** (pot - 1)
	module = (index - cluster) % pot

	return int(str(number)[module])

queries = int(input())
results = []
for query in range(queries):
	results.append(solve(int(input())))

print(*results, sep="\n")