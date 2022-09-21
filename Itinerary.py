import heapq

from sys import stdin, stdout
import sys

from Parser import Parser
from Graph import Graph

class Itinerary:
	def __init__(self, graph, station1, station2):
		
		with open('./_dataset/london.connections.csv', newline='') as london_connections:
			print(london_connections)
		return 'Object Initialized'
	
	def D_ShortestPath(self, graph, station1, station2):
		# Each station is represented as a node
		# Each line is represented as an edge
		# The weight of the edge is determined by the time 

		n = len(graph)
		visited = [False for x in range(n)]
		dist = [sys.maxsize for x in range(n)]
		dist[station1] = 0
		
		pq = [(0, station1)]

		while len(pq) > 0:
			weight, station = heapq.heappop(pq)		# discard weight for initial node
			if visited[station]: continue
			visited[station] = True

			for v, l in graph[station]:
				if dist[station] + l < dist[v]:
					dist[v] = dist[station] + l
					heapq.heappush(pq, (dist[v], v))

		return dist

	def A_ShortestPath(self, graph, start, stop):
		# A* algorithm
		g = {} #Actual movement cost from start to current station
		f = {} #Estimated movement cost from start to end through this station

		g[start] = 0
		f[start] = graph.heuristic(start, stop)

		closed = set()			#set for visited stations
		opened = set([start])	#set for unvisited stations
		adjacency = {}

		while len(opened) > 0:	#get the vertex from the open list with lowest f score
			current = None
			currentF = None
			for position in opened:
				if current is None or f[position] < currentF:
					currentF = f[position]
					current = position

			if current == stop:	#check if goal is reached
				path = [current]
				while current in adjacency:
					current = adjacency[current]
					path.append(current)
				path.reverse()
				return path, f[stop]

			#Mark vertices as closed
			opened.remove(current)
			closed.add(current)


			#Update neighbour scores
			for neighbour in graph.adjacent_nodes(current):
				if neighbour in closed:
					continue
				newG = g[current] + graph.heuristic(current, neighbour)

				if neighbour not in opened:
					opened.add(neighbour)
				elif newG >= g[neighbour]:
					continue

				adjacency[neighbour] = current
				g[neighbour] = newG
				h = graph.heuristic(neighbour, stop)
				f[neighbour] = g[neighbour] + h

		raise RuntimeError("A* did not find a solution")

	def main(input_stream, output_stream):

		parsed_file = Parser()
		lines = parsed_file.get_lines()
		connections = parsed_file.get_connections()
		stations = parsed_file.get_stations()
		graph = Graph(connections)
		
		#print(graph.total_nodes())
		#print(graph.adjacent_nodes(130))
		
	
	if __name__ == "__main__":
		main(stdin, stdout)
		parsed_file = Parser()
		connections = parsed_file.get_connections()
		graph = Graph(connections)


		#print(graph.total_nodes())
		#A_ShortestPath(None, graph, 11, 163)
