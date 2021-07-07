def solve(index):
	if index < 10:
	 	return index

	sector = 10
	cluster = 0
	while True:
		cluster += 1
		track = sector + ((10 ** cluster) * 9) * (cluster + 1)
		if track > index:
			cluster += 1
			break
		sector = track

	i = (index - sector) // cluster
	number = i + 10 ** (cluster - 1)
	module = (index - sector) % cluster

	return int(str(number)[module])

queries = int(input())
results = []
for query in range(queries):
	results.append(solve(int(input())))

print(*results, sep="\n")