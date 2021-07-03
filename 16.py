def solve(divL, divR, numbers):
	if len(numbers) == 0:
		return abs(divL - divR)
	else:
		sumL = solve(divL + numbers[0], divR, numbers[1:])
		sumR = solve(divL, divR + numbers[0], numbers[1:])
		return(min(sumL, sumR))

n = int(input())
arr = list(map(int, input().split()))
print(solve(0, 0, arr))