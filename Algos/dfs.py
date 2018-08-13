import collections

def depth_first_search(graph, source):

	visited, stack = [], [source]

	while stack:
		vertex = stack.pop()
		visited.append(vertex)

		for neighbour in graph[vertex]:
			if neighbour not in visited:	
				stack.append(neighbour)
						
	print(visited)

def add_edge(graph, u, v):
	graph[u].append(v)
	return graph


if __name__ == '__main__':

	# Creating the graph
	graph = collections.defaultdict(list)
	graph = add_edge(graph, 1, 0)
	graph = add_edge(graph, 2, 1)
	graph = add_edge(graph, 0, 3)
	graph = add_edge(graph, 0, 2)
	graph = add_edge(graph, 3, 4)
	graph = add_edge(graph, 4, 0)

	#print(graph)
	#graph = {1: [2, 3], 2: [4, 5], 3: [5], 4: [6], 5: [6], 6: [7], 7: []}
	#graph = {0: [1, 3, 2], 1: [4, 6], 2: [3, 5], 3: [4], 4: [], 5: [], 6: []}
	depth_first_search(graph, 0)