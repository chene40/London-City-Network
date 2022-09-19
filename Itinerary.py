import csv

from sys import stdin, stdout

class Itinerary:
	def __init__(self):
		with open('./_dataset/london.connections.csv', newline='') as london_connections:
			print(london_connections)
		return 'Object Initialized'
	
	def D_ShortestPath(self, source, target):
		# Dijkstra's algorithm
		shortest_distances = []

		return 'Dijkstra\'s Algorithm'

	def A_ShortestPath(self, source, target):
		# A* algorithm
		return 'A* Algorithm'

	def main(input_stream, output_stream):

		# should probably encapsulate all the parsing into another class/file
		
		# parsing london.lines.csv
		with open('./_dataset/london.lines.csv', newline='') as london_lines:
			parsed_london_lines = london_lines.read().replace('"', "").strip().split("\n")
			london_lines_header = parsed_london_lines[0].split(",")
			print(london_lines_header)

			for i in range(1, len(parsed_london_lines)):
				entry = parsed_london_lines[i].split(",")
				entry[0] = int(entry[0])
				print(entry)

		# parsing london.connections.csv
		with open('./_dataset/london.connections.csv', newline='') as london_connections:
			parsed_london_connections = london_connections.read().strip().split("\n")
			london_connection_headers = parsed_london_connections[0].replace('"', "").split(",")
			print(london_connection_headers)

			for i in range(1, len(parsed_london_connections)):
				print([int(x) for x in parsed_london_connections[i].split(",")])

		# parsing london.stations.csv
		with open('./_dataset/london.stations.csv', newline='') as london_stations:
			parsed_london_stations = london_stations.read().replace('"', "").strip().split("\n")
			london_stations_headers = parsed_london_stations[0].split(",")
			print(london_stations_headers)

			for i in range(1, len(parsed_london_stations)):
				""" entry = parsed_london_stations[i].strip().replace("<br />", "").split(",") """
				entry = parsed_london_stations[i].strip().split(",")
				entry[0] = int(entry[0])
				entry[1] = float(entry[1])
				entry[2] = float(entry[2])
				entry[-1] = int(entry[-1])
				entry[-2] = int(entry[-2])
				entry[-3] = float(entry[-3])
				print(entry)
	
	if __name__ == "__main__":
		main(stdin, stdout)
