import sys

from Node import Node

class Graph(object):
	def __init__(self, graph):
		self.nodes = {}
		self.create_connections(graph)
		self.graph = self.create_graph(self.nodes.items())
	
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

	def create_graph(self, nodes):
		graph = {}
		for node in nodes: 
			print(node)
			graph.update({node: node[1].stations()})
		return graph
	
	def adjacent_nodes(self, node): return self.graph[node].stations().keys()

	def total_nodes(self): return len(self.nodes)