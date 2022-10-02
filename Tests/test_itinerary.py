import sys

sys.path.insert(0, "./Itinerary")
sys.path.insert(0, "./Itinerary/GraphBuilder")
sys.path.insert(0, "./Itinerary/Utils")

from Itinerary import Itinerary  # noqa: E402
from Parser import Parser  # noqa: E402
from Graph import Graph  # noqa: E402

parsed_file = Parser()
connections = parsed_file.get_connections()
graph = Graph(connections)

itinerary = Itinerary(graph)


def test_A():
    result1 = itinerary.A_ShortestPath(2, 3)
    assert result1.get("Path") == [2, 263, 3]
    result1reverse = itinerary.A_ShortestPath(3, 2)
    assert result1reverse.get("Path") == [3, 263, 2]

    result2 = itinerary.A_ShortestPath(3, 4)
    assert result2.get("Path") == [3, 295, 225, 155, 284, 201, 4]
    result2reverse = itinerary.A_ShortestPath(4, 3)
    assert result2reverse.get("Path") == [4, 201, 284, 155, 225, 295, 3]

    result3 = itinerary.A_ShortestPath(5, 1)
    assert result3.get("Path") == [5, 194, 182, 73, 1]
    result3reverse = itinerary.A_ShortestPath(1, 5)
    assert result3reverse.get("Path") == [1, 73, 182, 194, 5]


def test_dijkstra():
    result1 = itinerary.D_ShortestPath(2, 3)
    assert result1.get("Path") == [2, 263, 3]
    assert result1.get("Distance") == 6
    result1reverse = itinerary.D_ShortestPath(3, 2)
    assert result1reverse.get("Path") == [3, 263, 2]
    assert result1reverse.get("Distance") == 6

    result2 = itinerary.D_ShortestPath(3, 4)
    assert result2.get("Path") == [3, 295, 225, 155, 284, 201, 4]
    assert result2.get("Distance") == 12
    result2reverse = itinerary.D_ShortestPath(4, 3)
    assert result2reverse.get("Path") == [4, 201, 284, 155, 225, 295, 3]
    assert result2reverse.get("Distance") == 12

    result3 = itinerary.D_ShortestPath(5, 1)
    assert result3.get("Path") == [5, 194, 182, 73, 1]
    assert result3.get("Distance") == 10
    result3reverse = itinerary.D_ShortestPath(1, 5)
    assert result3reverse.get("Path") == [1, 73, 182, 194, 5]
    assert result3reverse.get("Distance") == 10
