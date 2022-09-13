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
		with open('./_dataset/london.lines.csv', newline='') as london_lines:
			dataSemiParsed = london_lines.read().strip().split('\n')
			for entry in dataSemiParsed:
				entry.split(',')
				print([entry])
			# print(dataSemiParsed)
		return ''
	
	if __name__ == "__main__":
		main(stdin, stdout)
