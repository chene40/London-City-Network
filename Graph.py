import sys

import Node

class Graph(object):
	def __init__(self, nodes, initial_graph):
		self.nodes = {}
		self.create_connections(initial_graph)
		self.graph = self.create_graph(nodes, initial_graph)
	
	def create_connections(self, graph):

		for entry in graph:
			station1 = entry[0]
			station2 = entry[1]
			line = entry[2]
			weight = entry[3]

			if not station1 in self.nodes:
				connectionA = Node(station1)
				connectionA.update_node(station2, line, weight)
				self.nodes.update({station1: connectionA})
			else:
				self.nodes[station1].update_node(station2, line, weight)

			if not station2 in self.nodes:
				connectionB = Node(station2)
				connectionB.update_node(station1, line, weight)
				self.nodes.update({station2: connectionB})
			else:
				self.nodes[station2].update_node(station1, line, weight)


	def create_graph(self, nodes, initial_graph):
		graph = {}
		for node in nodes: graph[node] = {}	
		graph.update(initial_graph)

		for node, edges in graph.items():
			for nb_node, weight in edges.items():
				if not graph[nb_node].get(node, False): graph[nb_node][node] = weight
		return graph
	
	def adjacent_nodes(self, node):
		neighbours = []
	
		for nb in self.nodes:
			if self.graph[node].get(nb, False): neighbours.append(nb)

		return neighbours

	def num_nodes(self): return self.nodes
	def weight(self, node1, node2): return self.graph[node1][node2]
