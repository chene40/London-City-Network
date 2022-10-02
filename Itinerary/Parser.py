class Parser(object):
    def __init__(self):
        self.lines = self.london_lines()
        self.connections = self.london_connections()
        self.stations = self.london_stations()

    def london_lines(self):
        lines_list = []
        with open("./_dataset/london.lines.csv", newline="") as lines:
            parsed_lines = lines.read().replace('"', "").strip().split("\n")
            for i in range(len(parsed_lines)):
                entry = parsed_lines[i].split(",")
                if i > 0:
                    entry[0] = int(entry[0])
                lines_list.append(entry)
        return lines_list

    def london_connections(self):
        cons_list = []
        # parsing london.connections.csv
        with open("./_dataset/london.connections.csv", newline="") as cons:
            parsed_cons = cons.read().strip().split("\n")
            cons_list.append(parsed_cons[0].replace('"', "").split(","))
            for i in range(1, len(parsed_cons)):
                cons_list.append([int(x) for x in parsed_cons[i].split(",")])
        return cons_list

    def london_stations(self):
        stations_list = []
        # parsing london.stations.csv
        with open("./_dataset/london.stations.csv", newline="") as stns:
            parsed_stations = stns.read().replace('"', "").strip().split("\n")

            for i in range(len(parsed_stations)):
                entry = parsed_stations[i].strip().split(",")
                if i == 0:
                    stations_list.append(entry)
                    continue
                entry[0] = int(entry[0])
                entry[1] = float(entry[1])
                entry[2] = float(entry[2])
                entry[-1] = int(entry[-1])
                entry[-2] = int(entry[-2])
                entry[-3] = float(entry[-3])
                stations_list.append(entry)

        return stations_list

    def get_lines(self):
        return self.lines

    def get_connections(self):
        return self.connections

    def get_stations(self):
        return self.stations
