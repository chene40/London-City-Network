import csv

class Parser(object):

	def __init__(self):
		self.lines = self.london_lines()
		self.connections = self.london_connections()
		self.stations = self.london_stations()

	def london_lines(self):
		lines = []
		with open('./_dataset/london.lines.csv', newline='') as london_lines:
			parsed_london_lines = london_lines.read().replace('"', "").strip().split("\n")
			for i in range(len(parsed_london_lines)):
				entry = parsed_london_lines[i].split(",")
				if (i > 0): entry[0] = int(entry[0])
				lines.append(entry)
		return lines
			
	def london_connections(self):
		connections = []
		# parsing london.connections.csv
		with open('./_dataset/london.connections.csv', newline='') as london_connections:
			parsed_london_connections = london_connections.read().strip().split("\n")
			connections.append(parsed_london_connections[0].replace('"', "").split(","))
			for i in range(1, len(parsed_london_connections)): connections.append([int(x) for x in parsed_london_connections[i].split(",")])
		return connections
	
	def london_stations(self):
		stations = []
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

		return stations
	
	def get_lines(self): 
		return self.lines

	def get_connections(self): 
		return self.connections

	def get_stations(self): 
		return self.stations