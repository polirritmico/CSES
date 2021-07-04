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
		global solutions
		solutions += 1
	else:
		for i in range(8):
			queens[level] = i
			if is_valid(queens, board, level):
				solve(queens, board, level + 1)


board = [input() for line in range(8)]
queens = [-1 for x in range(8)]
solutions = 0

solve(queens, board, 0)
print(solutions)
