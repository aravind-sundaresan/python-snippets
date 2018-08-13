import collections

def breadth_first_search(graph, source):

	visited, queue = [], collections.deque([source])
	visited.append(source)

	while queue:
		vertex = queue.popleft()
		for neighbour in graph[vertex]:
			if neighbour not in visited:
				queue.append(neighbour)
				visited.append(neighbour)

	print(visited)

def add_edge(graph, u, v):
	graph[u].append(v)
	return graph


if __name__ == '__main__':

	# Creating the graph
	graph = collections.defaultdict(list)
	graph = add_edge(graph, 0, 1)
	graph = add_edge(graph, 0, 2)
	graph = add_edge(graph, 1, 2)
	graph = add_edge(graph, 2, 0)
	graph = add_edge(graph, 2, 3)
	graph = add_edge(graph, 3, 3)

	#graph = {0: [1, 3, 2], 1: [4, 6], 2: [3, 5], 3: [4], 4: [], 5: [], 6: []}
	breadth_first_search(graph, 1)