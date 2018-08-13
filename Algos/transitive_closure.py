def transitive_closure(n, adjacency_matrix):

	a = adjacency_matrix

	for k in range(n):
		for i in range(n):
			for j in range(n):
				if (a[i][j] == 0):
					if a[i][k] == 1 and a[k][j] == 1:
						a[i][j] = 1

	return a

if __name__ == '__main__':
	n = 4
	adjacency_matrix = [[0, 1, 0, 0], [0, 0, 0, 1], [0, 0, 0, 0], [1, 0, 1, 0]]

	output_matrix = transitive_closure(n, adjacency_matrix)

	for i in range(n):
		for j in range(n):
			print(str(output_matrix[i][j]) + " ", end='')
		print("\n")
