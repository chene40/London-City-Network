import sys

sys.path.insert(0, "./Itinerary")
from Graph import Graph  # noqa: E402
from Parser import Parser  # noqa: E402

connection = Parser().get_connections()
graph = Graph(connection)


def test_adjacent_nodes():
    assert list(graph.adjacent_nodes(1)) == [52, 73, 234, 265]
    assert list(graph.adjacent_nodes(10)) == [95, 128]
    assert list(graph.adjacent_nodes(100)) == [34, 111]


def test_distance():
    # must be adjacent stations in order to find distance between them
    assert graph.get_distance(100, 34) == 3
    assert graph.get_distance(100, 111) == 4

    assert graph.get_distance(34, 100) == 3
    assert graph.get_distance(111, 100) == 4

    assert graph.get_distance(100, 100) == 0


def test_find_coords():
    assert graph.find_coordinates(50) == [51.7052, -0.611]
    assert graph.find_coordinates(100) == [51.5724, -0.1941]
    assert graph.find_coordinates(150) == [51.5139, -0.2172]
    assert graph.find_coordinates(200) == [51.5313, 0.0172]
    assert graph.find_coordinates(250) == [51.5146, -0.0973]


test_adjacent_nodes()
test_distance()
test_find_coords()
