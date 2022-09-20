import csv

import heapq

from sys import stdin, stdout
import sys

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

	def A_ShortestPath(self, source, target):
		# A* algorithm
		return 'A* Algorithm'

	def main(input_stream, output_stream):

		# should probably encapsulate all the parsing into another class/file

		lines = []
		connections = []
		stations = []
		
		# parsing london.lines.csv
		with open('./_dataset/london.lines.csv', newline='') as london_lines:
			parsed_london_lines = london_lines.read().replace('"', "").strip().split("\n")
			for i in range(len(parsed_london_lines)):
				entry = parsed_london_lines[i].split(",")
				if (i > 0): entry[0] = int(entry[0])
				lines.append(entry)
			
		# parsing london.connections.csv
		with open('./_dataset/london.connections.csv', newline='') as london_connections:
			parsed_london_connections = london_connections.read().strip().split("\n")
			connections.append(parsed_london_connections[0].replace('"', "").split(","))
			for i in range(1, len(parsed_london_connections)): connections.append([int(x) for x in parsed_london_connections[i].split(",")])

		# parsing london.stations.csv
		with open('./_dataset/london.stations.csv', newline='') as london_stations:
			parsed_london_stations = london_stations.read().replace('"', "").strip().split("\n")

			for i in range(len(parsed_london_stations)):
				""" entry = parsed_london_stations[i].strip().replace("<br />", "").split(",") """
				entry = parsed_london_stations[i].strip().split(",")
				if (i == 0): 
					stations.append(entry)
					continue
				entry[0] = int(entry[0])
				entry[1] = float(entry[1])
				entry[2] = float(entry[2])
				entry[-1] = int(entry[-1])
				entry[-2] = int(entry[-2])
				entry[-3] = float(entry[-3])
				stations.append(entry)
			print(stations)
	
	if __name__ == "__main__":
		main(stdin, stdout)
