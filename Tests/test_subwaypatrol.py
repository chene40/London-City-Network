import sys

sys.path.insert(0, "./Itinerary")
from SubwayPatrol import SubwayPatrol  # noqa: E402
from Parser import Parser  # noqa: E402
from Graph import Graph  # noqa: E402
from Itinerary import Itinerary  # noqa: E402

parsed_file = Parser()
connections = parsed_file.get_connections()
newGraph = Graph(connections)
itinerary = Itinerary(newGraph)
patrol = SubwayPatrol(newGraph, itinerary)


def test():
    result1 = patrol.ShortestPath([1, 2, 3, 4, 5], 2)
    result2 = patrol.ShortestPath([1, 2, 3, 4, 5, 6], 2)
    result3 = patrol.ShortestPath([1, 2, 3, 4, 5], 5)

    assert result1.get("Path") == [2, 1, 3, 4, 5]
    assert result1.get("Distance") == 65

    assert result2.get("Path") == [2, 1, 3, 4, 5, 6]
    assert result2.get("Distance") == 109

    assert result3.get("Path") == [5, 1, 2, 3, 4]
    assert result3.get("Distance") == 59


test()
