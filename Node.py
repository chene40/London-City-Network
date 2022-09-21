import sys
from Parser import Parser

parsed_file = Parser()
stations = parsed_file.get_stations()

class Node(object):
	def __init__(self, station1):
		self.station_name = station1
		self.connected_stations = {}
		for node in stations:
			if self.station_name == node[0]:
				self.coordinates = [node[1], node[2]]
	
	def update_node(self, connected_station, line, weight):
		entry = {connected_station: [line, weight]}
		self.connected_stations.update(entry)

	def get_coordinates(self): return self.coordinates

	def get_name(self): return self.station_name
	
	def stations(self): return self.connected_stations
