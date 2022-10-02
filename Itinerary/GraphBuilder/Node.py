import sys

sys.path.insert(0, "./Itinerary/Utils")

# Local Files
from Parser import Parser


parsed_file = Parser()
stations = parsed_file.get_stations()


class Node(object):
    def __init__(self, stationId: int):
        self.station_name = stationId
        self.connected_stations = {}
        self.set_coordinates(stationId)

    def update(self, connected_station: int, line: int, weight: int):
        entry = {connected_station: [line, weight]}
        self.connected_stations.update(entry)

    def set_coordinates(self, stationId: int):
        for entry in stations:
            if entry[0] == stationId:
                self.coordinates = [entry[1], entry[2]]
                break

    def remove(self, station: int):
        if station in self.connected_stations.keys():
            self.connected_stations.pop(station)

    def get_coordinates(self):
        return self.coordinates

    def get_name(self):
        return self.station_name

    def stations(self):
        return self.connected_stations
