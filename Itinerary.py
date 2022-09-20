import heapq

from sys import stdin, stdout
import sys

from Parser import Parser
from Graph import Graph

class Itinerary:
	def __init__(self):
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
		open_set = set(start)
		closed_set = set()
		g = {}
		parents = {}
		g[start] = 0
		parents[start] = start
		while len(open_set) > 0:
			n = None
			for v in open_set:
				if n == None or g[v] + graph.weight(start,v) < g[n] + graph.weight(start,n):
					n = v
			if n == stop or graph.nodes[n] == None:
				pass
			else:
				for (m, weight) in graph.adjacent_nodes[n]:
					if m not in open_set and m not in closed_set:
						open_set.add(m)
						parents[m] = n
						g[m] = g[n] + weight
					else:
						if g[m] > g[n] + weight:
							g[m] = g[n] + weight
							parents[m] = n
							if m in closed_set:
								closed_set.remove(m)
								open_set.add(m)
			if n == None:
				print('Path does not exist!')
				return None
			if n == stop:
				path = []
				while parents[n] != n:
					path.append(n)
					n = parents[n]
				path.append(start)
				path.reverse()
				print('Path found: {}'.format(path))
				return path
			open_set.remove(n)
			closed_set.add(n)
		print('Path does not exist!')
		return None

	def main(input_stream, output_stream):

		parsed_file = Parser()
		#lines = parsed_file.get_lines()
		connections = parsed_file.get_connections()
		#stations = parsed_file.get_stations()

		graph = Graph(connections)
		print(graph.total_nodes())
		#print(graph.adjacent_nodes(130))
	
	if __name__ == "__main__":
		main(stdin, stdout)
