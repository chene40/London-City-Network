import sys
from Parser import Parser

parsed_file = Parser()
stations = parsed_file.get_stations()

class Node(object):
	def __init__(self, station1):
		self.station_name = station1
		self.connected_stations = {}
		for entry in stations:
			if entry[0] == station1:
				self.coordinates = [entry[1], entry[2]]
				break
	
	def update_node(self, connected_station, line, weight):
		entry = {connected_station: [line, weight]}
		self.connected_stations.update(entry)

	def get_coordinates(self): return self.coordinates

	def get_name(self): return self.station_name
	
	def stations(self): return self.connected_stations