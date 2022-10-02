from Parser import Parser
from Graph import Graph


class UrbanismPlanning:
    def __init__(self, graph: Graph, stations: list):
        self.zones = {}  # {zone#: [station1, stations2, ...]}
        self.islands = {}  # {zone#: [[island1], [island2]], ... }

        self.graph = graph
        self.stations = stations
        self.create_zones()
        self.create_islands()

    def create_zones(self):
        for i in range(1, len(self.stations)):
            station_entry = self.stations[i]
            stationId = station_entry[0]
            zone = station_entry[5]

            if zone in self.zones.keys():
                self.zones[zone].append(stationId)
            else:
                entry = {zone: [stationId]}
                self.zones.update(entry)

        """ check parser file and fix this odd-looking entry """
        self.zones.pop("Heathrow<br />Terminals<br />1")
        self.zones[6].append(117)

    def get_zones(self):
        return self.zones

    def num_zones(self):
        # print(f"The number of different zones is: {len(self.zones.keys())}.")
        return len(self.zones.keys())

    def get_stations_in_zone(self, zone: int):
        print(f"The stations in zone {zone} are {self.zones.get(zone)}.")
        return self.zones.get(zone)

    def islandDFS(self, temp: list, node: int, visited: list, nodeZone: float):
        visited[node] = True
        temp.append(node)

        for node in self.graph.adjacent_nodes(node):
            for key, value in self.zones.items():
                if node in value:
                    currNodeZone = key

            if currNodeZone != nodeZone:
                continue

            if not visited[node]:
                temp = self.islandDFS(temp, node, visited, nodeZone)
        return temp

    def create_islands(self):
        visited = [False for _ in range(len(self.graph.get_nodes()) + 2)]
        islands = []

        for node in self.graph.get_nodes_name():
            for key, value in self.zones.items():
                if node in value:
                    nodeZone = key

            if not visited[node]:
                temp = []
                islands.append(
                    {nodeZone: self.islandDFS(temp, node, visited, nodeZone)}
                )

        for island in islands:
            for key in island.keys():
                zone = key

            if zone not in self.islands.keys():
                for value in island.values():
                    newValue = value
                self.islands.update({zone: [newValue]})

            else:
                cc = self.islands.get(zone)
                for value in island.values():
                    cc.append(value)

    def get_islands(self):
        return self.islands

    def get_islands_in_zone(self, zone: int):
        return self.islands.get(zone)

    def num_islands_in_zone(self, zone: int):
        return len(self.islands.get(zone))

    def zone_of(self, station):
        for key, value in self.zones.items():
            if station in value:
                return key

    def connected_zones(self, zone: int):
        cZones = []

        zones = self.zones.get(zone)
        for z in zones:
            adjS = self.graph.adjacent_nodes(z)
            for node in adjS:
                z0 = self.zone_of(node)
                if z0 not in cZones and z0 != zone:
                    cZones.append(z0)
        return cZones


def main():
    parsed_file = Parser()
    connections = parsed_file.get_connections()
    stations = parsed_file.get_stations()
    # lines = parsed_file.get_lines()
    graph = Graph(connections)

    UB = UrbanismPlanning(graph, stations)
    zones = UB.get_zones()
    islands = UB.get_islands()

    for key, value in zones.items():
        print(f"Stations in zone {key}: {value}")

    for key, value in islands.items():
        print(f"Islands in zone {key}: {value}")

    print(UB.connected_zones(1))


if __name__ == "__main__":
    main()
