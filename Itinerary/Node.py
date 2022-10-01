# Python Library
import sys

# Local Files
from Parser import Parser

parsed_file = Parser()
stations = parsed_file.get_stations()

class Node(object):
	def __init__(self, stationId):
		self.station_name = stationId
		self.connected_stations = {}
		self.set_coords(stationId)
	
	def update_node(self, connected_station, line, weight):
		entry = {connected_station: [line, weight]}
		self.connected_stations.update(entry)

	def set_coords(self, stationId): 
		for entry in stations:
			if entry[0] == stationId:
				self.coordinates = [entry[1], entry[2]]
				break

	def get_coordinates(self): return self.coordinates
	
	def get_name(self): return self.station_name
	
	def stations(self): return self.connected_stations
