def solve(input_str):
	input_str = input_str.split()
	pile_a = int(input_str[0])
	pile_b = int(input_str[1])
 
	if pile_b > pile_a:
		pile_a, pile_b = pile_b, pile_a
 
	if pile_a <= 2 * pile_b:
		a = pile_a % 3
		b = pile_b % 3
		if b > a:
			a, b = b, a
 
		if (a == b and a == 0) or (a == 2 * b and a != 1):
			return "YES"
	return "NO"


solutions = []
for i in range(int(input())):
	solutions.append(solve(input()))

print(*solutions, sep="\n")