# Python Library
from math import sqrt

# Local Files
from Node import Node

class Graph(object):
	def __init__(self, graph):
		self.nodes = {}
		self.create_connections(graph)
	
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
	
	def adjacent_nodes(self, node): return self.nodes[node].stations().keys()

	def get_nodes(self): return self.nodes

	def get_nodes_name(self): return [node for node in self.nodes if isinstance(node, int)]

	def get_distance(self, station1, station2):
		s1 = self.nodes[station1]
		s2 = self.nodes[station2]

		return s2.stations()[s1.get_name()][1]
		
	def heuristic(self, start, goal):
		startNode = self.nodes[start]
		goalNode = self.nodes[goal]
		startNodeCoords = startNode.get_coordinates()
		goalNodeCoords = goalNode.get_coordinates()

		distX = abs(startNodeCoords[0] - goalNodeCoords[0])
		distY = abs(startNodeCoords[1] - goalNodeCoords[1])
		return (sqrt(distX**2 + distY**2))

	def find_coordinates(self, stationID):
		for node in self.nodes:
			if node == stationID:
				coordinates = self.nodes[stationID].get_coordinates()
				return coordinates
		return "Node not found"