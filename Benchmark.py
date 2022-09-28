import random
from Itinerary import Itinerary 
import time
from Parser import Parser
from Graph import Graph

# Wall Time
class Benchmark:
	def __init__(self):

		self.parsed_file = parsed_file = Parser()
		self.connections = parsed_file.get_connections()
		self.graph = Graph(self.connections)
		self.itinerary = Itinerary(self.graph)
		self.station1 = random.randint(1, 303); self.station2 = random.randint(1, 303)

		while (self.station1 == self.station2):
			self.station2 = random.randint(1, 303)

	def WallTime(self):
		A_start = time.time()
		self.itinerary.A_ShortestPath(self.graph,self.station1, self.station2)
		A_end = round(time.time() - A_start, 5)
		#print(f"A* Algorithm Wall-Time is {A_end} seconds")

		D_start = time.time()
		self.itinerary.D_ShortestPath(self.graph,self.station1, self.station2)
		D_end = round(time.time() - D_start, 5)
		#print(f"Dijkstra's Algorithm Wall-Time is {D_end} seconds")

		return (A_end, D_end)
	
	def CPUTime(self):
		A_start = time.process_time()
		self.itinerary.A_ShortestPath(self.graph,self.station1, self.station2)
		A_end = round(time.process_time() - A_start, 5)
		#print(f"A* Algorithm CPU-Time is {A_end} seconds")

		D_start = time.process_time()
		self.itinerary.D_ShortestPath(self.graph,self.station1, self.station2)
		D_end = round(time.process_time() - D_start, 6)
		#print(f"Dijkstra's Algorithm CPU-Time is {D_end} seconds")

		return (A_end, D_end)

	def test(self, numTests):

		A_WallTime = 0; D_WallTime = 0
		A_CPUTime = 0; D_CPUTime = 0

		for i in range(numTests):
			Wall_Time = self.WallTime()
			A_WallTime += Wall_Time[0]
			D_WallTime += Wall_Time[1]

			CPU_Time = self.WallTime()
			A_CPUTime += CPU_Time[0]
			D_CPUTime += CPU_Time[1]

		A_WallTime /= numTests; D_WallTime /= numTests
		A_CPUTime /= numTests; D_CPUTime /= numTests
		
		return {
			'Average Wall Time - A* Algorithm': A_WallTime,
			'Average Wall Time - Dijkstra\'s Algorithm': D_WallTime,
			'Average CPU Time - A* Algorithm': A_CPUTime,
			'Average CPU Time - Dijkstra\'s Algorithm': D_CPUTime,
		}

if __name__ == "__main__":
	benchmark = Benchmark()
	#benchmark.CPUTime()
	#benchmark.WallTime()
	print(benchmark.test(100))