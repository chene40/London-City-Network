from Parser import Parser
from Graph import Graph
from sys import maxsize
from itertools import permutations
from Itinerary import Itinerary


class SubwayPatrol:
    def __init__(self, graph, itinerary):
        self.graph = graph
        self.itinerary = itinerary

    def ShortestPath(self, allStations, startStation):

        shortestPath = [startStation]
        allStations.remove(startStation)
        path = maxsize
        nextPerm = permutations(allStations)
        for nextStation in nextPerm:
            currentWeight = 0
            currentStation = startStation

            for station in nextStation:
                shortestDist = maxsize
                dist = self.itinerary.D_ShortestPath(currentStation, station)
                distanceValues = list(dist.items())
                if distanceValues[1][1] < shortestDist:
                    currentStation = station
                    shortestDist = distanceValues[1][1]

                currentWeight += shortestDist
                if currentStation not in shortestPath:
                    shortestPath.append(currentStation)
            path = min(path, currentWeight)

        return {"Path": shortestPath, "Distance": path}


def main():
    parsed_file = Parser()
    connections = parsed_file.get_connections()
    newGraph = Graph(connections)
    itinerary = Itinerary(newGraph)
    patrol = SubwayPatrol(newGraph, itinerary)

    print(patrol.ShortestPath([1, 2, 3, 4, 5], 2))


if __name__ == "__main__":
    main()
