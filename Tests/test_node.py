import sys

sys.path.insert(0, "./Itinerary/GraphBuilder")

from Node import Node  # noqa: E402


def test_name():
    node1 = Node(1)
    node10 = Node(10)
    node100 = Node(100)
    nodeD = Node(1.5)
    nodeS = Node("Hello World")
    assert node1.get_name() == 1
    assert node10.get_name() == 10
    assert node100.get_name() == 100
    assert nodeD.get_name() == 1.5
    assert nodeS.get_name() == "Hello World"


def test_coordinates():
    node10 = Node(10)
    assert node10.get_coordinates() == [51.5586, -0.1059]

    node20 = Node(20)
    assert node20.get_coordinates() == [51.5087, 0.055]


def test_stations():
    node = Node(100)
    node.update(34, 9, 3)
    assert node.stations() == {34: [9, 3]}

    node.update(10, 20, 30)
    assert node.stations() == {34: [9, 3], 10: [20, 30]}

    node.remove(10)
    assert node.stations() == {34: [9, 3]}

    node.remove(34)
    assert node.stations() == {}
