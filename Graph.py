import sys

class Graph(object):
	def __init__(self, nodes, initial_graph):
		self.nodes = nodes
		self.graph = self.create_graph(nodes, initial_graph)
	
	def create_graph(self, nodes, initial_graph):
		# dictionary {} i.e. key-value pairs
		graph = {}

		# initializes all keys (i.e. cities) in the graph with null dictionary values (i.e. all connected cities)
		for node in nodes: graph[node] = {}	

		# puts the key-value pairs into the graph (dictionary)
		graph.update(initial_graph)

		# .items() return all key-value pairs in a dictionary
		for node, edges in graph.items():			# key: node (city), value: edges (dictionary itself containing all edges/connected cities)
			for nb_node, weight in edges.items():		# key: neighbour node, value: weight of each edge
				if not graph[nb_node].get(node, False): graph[nb_node][node] = weight
		return graph
	
	
	def adjacent_nodes(self, node):
		neighbours = []
	
		for nb in self.nodes:
			# if neighbor node is not found, add it to the list of neighbors nodes
			if self.graph[node].get(nb, False): neighbours.append(nb)

		return neighbours

	def num_nodes(self): return self.nodes		# get total num of nodes in graph

	def weight(self, node1, node2): return self.graph[node1][node2]			# get the weighting between two nodes
