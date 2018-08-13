def all_pairs_shortest_path(n, cost_adjacency_matrix):

	for k in range(n):
		for i in range(n):
			for j in range(n):
				cost_adjacency_matrix[i][j] = min(cost_adjacency_matrix[i][j], (cost_adjacency_matrix[i][k] + cost_adjacency_matrix[k][j]))
		print(cost_adjacency_matrix)

	return cost_adjacency_matrix

if __name__ == '__main__':
	n = 4
	cost_adjacency_matrix = [[0, 999, 3, 999], [2, 0, 999, 999], [999, 7, 0, 1], [6, 999, 999, 0]]
	output_matrix = all_pairs_shortest_path(n, cost_adjacency_matrix)

	for i in range(n):
		for j in range(n):
			print(str(output_matrix[i][j]) + " ", end='')
		print("\n")