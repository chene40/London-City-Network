import heapq

from sys import maxsize, stdin, stdout
import sys

from Parser import Parser
from Graph import Graph

class Itinerary:
	def __init__(self, graph):
		self.graph = graph
	
	def D_ShortestPath(self, graph, station1, station2):

		stationNames = graph.get_nodes_name()

		visited = {node: False for node in stationNames}
		dist = {node: sys.maxsize for node in stationNames}
		prevNode = {node: 0 for node in stationNames }

		dist[station1] = 0
		prevNode[station1] = station1
		pq = [(0, station1)]

		while len(pq) > 0:
			weight, station = heapq.heappop(pq)
			if visited[station]: continue
			visited[station] = True

			for adj_station in graph.adjacent_nodes(station):
				distance = graph.get_distance(station, adj_station)
				if dist[station] + distance < dist[adj_station]:
					dist[adj_station] = dist[station] + distance
					heapq.heappush(pq, (dist[adj_station], adj_station))
					prevNode[adj_station] = station

		shortest_path = []
		lastStation = station2

		while(lastStation != station1):
			shortest_path.insert(0, lastStation)
			lastStation = prevNode[lastStation]
		shortest_path.insert(0, station1)
		
		return {'Path': shortest_path, 'Distance': dist[station2]}

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
		connections = parsed_file.get_connections()
				
	if __name__ == "__main__":
		main(stdin, stdout)
		parsed_file = Parser()
		connections = parsed_file.get_connections()
		stations = parsed_file.get_stations()
		lines = parsed_file.get_lines()
		graph = Graph(connections)
		print(A_ShortestPath(None, graph,157,2))
		print(D_ShortestPath(None, graph, 1, 2))
		