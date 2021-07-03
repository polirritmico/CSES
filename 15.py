import itertools
s = input()
chset = []
for c in s:
	chset.append(c)
chset = list(dict.fromkeys(itertools.permutations(chset)))
chset = sorted(chset)
print(len(chset))
for s in chset:
	for c in s:
		print(c, end="")
	print()
