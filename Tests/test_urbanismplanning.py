import sys

sys.path.insert(0, "./Itinerary")
sys.path.insert(0, "./Itinerary/GraphBuilder")
sys.path.insert(0, "./Itinerary/Utils")

from UrbanismPlanning import UrbanismPlanning  # noqa: E402
from Parser import Parser  # noqa: E402
from Graph import Graph  # noqa: E402

parsed_file = Parser()
connections = parsed_file.get_connections()
stations = parsed_file.get_stations()
graph = Graph(connections)

UB = UrbanismPlanning(graph, stations)


def test_num_zones():
    assert UB.num_zones() == 15


def test_get_zones():
    list_of_zones = [
        1,
        1.5,
        2,
        2.5,
        3,
        3.5,
        4,
        5,
        5.5,
        6,
        6.5,
        7,
        8,
        9,
        10,
    ]
    for zone in UB.get_zones().keys():
        assert zone in list_of_zones


def test_get_stations_in_zone():
    z6 = UB.get_stations_in_zone(6)
    z6.sort()
    z7 = UB.get_stations_in_zone(7)
    z7.sort()
    z8 = UB.get_stations_in_zone(8)
    z8.sort()
    z9 = UB.get_stations_in_zone(9)
    z9.sort()
    z10 = UB.get_stations_in_zone(10)
    z10.sort()

    assert z6 == [
        68,
        85,
        88,
        117,
        118,
        125,
        129,
        134,
        158,
        179,
        180,
        220,
        222,
        256,
        267,
        268,
        271,
        294,
    ]
    assert z7 == [62, 214]
    assert z8 == [53, 280]
    assert z9 == [46]
    assert z10 == [6, 50]


def test_get_islands_in_zone():
    islands6 = UB.get_islands_in_zone(6)
    islands7 = UB.get_islands_in_zone(7)
    islands8 = UB.get_islands_in_zone(8)
    islands9 = UB.get_islands_in_zone(9)
    islands10 = UB.get_islands_in_zone(10)

    assert islands6 == [
        [158, 68, 256, 88],
        [294],
        [85, 129, 268, 267],
        [222, 220, 134, 125, 271],
        [179, 180],
        [117, 118],
    ]
    assert islands7 == [[214], [62]]
    assert islands8 == [[53], [280]]
    assert islands9 == [[46]]
    assert islands10 == [[6], [50]]


def test_zone_of():
    station1 = 1
    station10 = 10
    station50 = 50
    station100 = 100
    station200 = 200

    assert UB.zone_of(station1) == 3
    assert UB.zone_of(station10) == 2
    assert UB.zone_of(station50) == 10
    assert UB.zone_of(station100) == 3
    assert UB.zone_of(station200) == 3


def test_connected_zones():
    assert UB.connected_zones(1) == [2.0, 1.5]
    assert UB.connected_zones(2) == [1.5, 2.5, 1.0, 4.0, 3.0]
    assert UB.connected_zones(3) == [2.5, 3.5, 4.0, 2.0]
    assert UB.connected_zones(4) == [3.0, 3.5, 5.0, 2.0]
    assert UB.connected_zones(5) == [4.0, 6.0, 5.5]
    assert UB.connected_zones(6) == [5.0, 5.5, 6.5]
    assert UB.connected_zones(7) == [6.5, 8.0]
    assert UB.connected_zones(8) == [9.0, 7.0]
    assert UB.connected_zones(9) == [10.0, 8.0]
    assert UB.connected_zones(10) == [9.0]
