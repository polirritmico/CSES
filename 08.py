n = int(input())
psbl = False
g1 = set()
g2 = set()
if n % 4 == 0:
	psbl = True
	i = 1
	way = True
	while i < n:
		if way:
			g1.add(i)
			g2.add(i+1)
		else:
			g2.add(i)
			g1.add(i+1)
		i += 2
		way = not way
elif (n - 3) % 4 == 0:
	psbl = True
	g1.add(1)
	g1.add(2)
	g2.add(3)
	i = 4
	while i < n:
		if (i // 4) % 2 == 0:
			g2.add(i)
			g1.add(i+1)
			g1.add(i+2)
			g2.add(i+3)
		else:
			g1.add(i)
			g2.add(i+1)
			g2.add(i+2)
			g1.add(i+3)
		i += 4
if not psbl:
	print("NO")
else:
	print("YES")
	print(len(g1))
	print(*g1)
	print(len(g2))
	print(*g2)