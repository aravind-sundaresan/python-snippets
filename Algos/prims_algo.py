def prims(n, cost_adjacency_matrix, source):

	mst = set() # Minimum Spanning Tree
	mst.add(source)

	weight = 0
	k = 1

	while(k < n):
		
		min_edge = 99
		for i in range(n):
			for j in range(n):
				if i in mst and j not in mst:
					if cost_adjacency_matrix[i][j] < min_edge:
						u = i
						v = j
						min_edge = cost_adjacency_matrix[i][j]

		mst.add(v)
		print(str(u) + " -> " + str(v))
		weight += min_edge
		k += 1

	print("Weight of the Minimum Spanning Tree = " + str(weight))


	return


if __name__ == '__main__':	

	n = 6  # Number of vertices
	cost_adjacency_matrix = [[0, 3, 99, 99, 6, 5], [3, 0, 1, 99, 99, 4], [99, 1, 0, 6, 99, 4], [99, 99, 6, 0, 8, 5], [6, 99, 99, 8, 0, 2], [5, 4, 4, 5, 2, 0]]
	source_vertex = 0

	prims(n, cost_adjacency_matrix, source_vertex)
