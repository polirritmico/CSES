n = int(input())
if n == 0:
	print(0)
pot = 2**n
for i in range(pot):
	s = ""
	for j in range(n-1, -1, -1):
		t = 2**j
		s += str(((i+t)//(t*2))%2)
	print(s)
