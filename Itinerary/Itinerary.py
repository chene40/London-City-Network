# Python Library
import heapq
from sys import maxsize

# Local Files
from Parser import Parser
from Graph import Graph


class Itinerary:
    def __init__(self, graph):
        self.graph = graph

    def D_ShortestPath(self, station1: int, station2: int):
        stationNames = self.graph.get_nodes_name()

        visited = {node: False for node in stationNames}
        dist = {node: maxsize for node in stationNames}
        prevNode = {node: 0 for node in stationNames}

        dist[station1] = 0
        prevNode[station1] = station1
        pq = [(0, station1)]

        while len(pq) > 0:
            weight, station = heapq.heappop(pq)
            if visited[station]:
                continue
            visited[station] = True

            for adj_station in self.graph.adjacent_nodes(station):
                distance = self.graph.get_distance(station, adj_station)
                if dist[station] + distance < dist[adj_station]:
                    dist[adj_station] = dist[station] + distance
                    heapq.heappush(pq, (dist[adj_station], adj_station))
                    prevNode[adj_station] = station

        shortest_path = []
        lastStation = station2

        while lastStation != station1:
            shortest_path.insert(0, lastStation)
            lastStation = prevNode[lastStation]
        shortest_path.insert(0, station1)

        return {"Path": shortest_path, "Distance": dist[station2]}

    def A_ShortestPath(self, start: int, stop: int):
        # A* algorithm

        g = {}  # Actual movement cost from start to current station
        f = {}  # Estimated movement cost from start to end through station

        g[start] = 0
        f[start] = self.graph.heuristic(start, stop)

        closed = set()  # set for visited stations
        opened = set([start])  # set for unvisited stations
        adjacency = {}

        # get the vertex from the open list with lowest f score
        while len(opened) > 0:
            current = None
            currentF = None
            for position in opened:
                if current is None or f[position] < currentF:
                    currentF = f[position]
                    current = position

            # check if goal is reached
            if current == stop:
                path = [current]
                while current in adjacency:
                    current = adjacency[current]
                    path.append(current)
                path.reverse()
                return {"Path": path, "Distance": f[stop]}

            # Mark vertices as closed
            opened.remove(current)
            closed.add(current)

            # Update neighbour scores
            for neighbour in self.graph.adjacent_nodes(current):
                if neighbour in closed:
                    continue
                newG = g[current] + self.graph.heuristic(current, neighbour)

                if neighbour not in opened:
                    opened.add(neighbour)
                elif newG >= g[neighbour]:
                    continue

                adjacency[neighbour] = current
                g[neighbour] = newG
                h = self.graph.heuristic(neighbour, stop)
                f[neighbour] = g[neighbour] + h

        raise RuntimeError("A* did not find a solution")


def main():
    parsed_file = Parser()
    connections = parsed_file.get_connections()
    # stations = parsed_file.get_stations()
    # lines = parsed_file.get_lines()
    graph = Graph(connections)

    itinerary = Itinerary(graph)
    print("A Star Algorithm")
    print("--------------------------------------")
    print(itinerary.A_ShortestPath(42, 53))
    print(itinerary.A_ShortestPath(21, 32))
    print(itinerary.A_ShortestPath(47, 14))
    print(itinerary.A_ShortestPath(93, 12))

    print("Dijkstra's Algorithm")
    print("--------------------------------------")
    print(itinerary.D_ShortestPath(42, 53))
    print(itinerary.D_ShortestPath(21, 32))
    print(itinerary.D_ShortestPath(47, 14))
    print(itinerary.D_ShortestPath(93, 12))


if __name__ == "__main__":
    main()
