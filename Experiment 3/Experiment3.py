def is_safe(r, c, n, board):
	# cols
	for i in range(r):
		if board[i][c] == 'M':
			return False

	# left diag
	i, j = r - 1, c - 1
	while i >= 0 and j >= 0:
		if  board[i][j] == 'M':
			return False
		i -= 1
		j -= 1

	# right diag
	i, j = r - 1, c + 1
	while i >= 0 and j < n:
		if board[i][j] == 'M':
			return False
		i -= 1
		j += 1

	return True

def solve(r, n, board):
	if r == n:
		return True

	for c in range(n):
		if is_safe(r, c, n, board):
			board[r][c] = 'M'
			if solve(r + 1, n, board):
				return [''.join(row) for row in board]
			board[r][c] = '.'

	return False

def main(n):
	board = [['.' for _ in range(n)] for _ in range(n)]

	return solve(0, n, board)

if __name__ == '__main__':
	print(main(4))
