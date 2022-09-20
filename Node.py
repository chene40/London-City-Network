import sys

class Node(object):
	def __init__(self, station1):
		self.station_name = station1
		self.connected_stations = {}
	
	def update_node(self, connected_station, line, weight):
		entry = {connected_station: {line, weight}}
		self.connected_stations.update(entry)
	
	def set_coordinates(self, lat, long): self.coords = [lat, long]

	def get_coordinates(self): return self.coords

	def get_name(self): return self.station_name
	
	def stations(self): return self.connected_stations
