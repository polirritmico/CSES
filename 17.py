def is_valid(queens, board, level):
	if board[level][queens[level]] == "*":
		return False
	for i in range(level):
		if queens[level] == queens[i]:
			return False
		if abs(level - i) == abs(queens[level] - queens[i]):
			return False
	return True


def solve(queens, board, level):
	if level == 8:
		return 1
	result = 0
	for i in range(8):
		queens[level] = i
		if is_valid(queens, board, level):
			result += solve(queens, board, level + 1)
	return result


board = [input() for line in range(8)]
queens = [-1 for x in range(8)]

print(solve(queens, board, 0))
