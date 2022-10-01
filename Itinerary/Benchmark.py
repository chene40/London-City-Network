# Python Library
import random
import time

# Local Files
from Itinerary import Itinerary
from Parser import Parser
from Graph import Graph

class Benchmark:
	def __init__(self):
		self.parsed_file = Parser()
		self.connections = self.parsed_file.get_connections()
		self.graph = Graph(self.connections)
		self.itinerary = Itinerary(self.graph)

		self.station1 = random.randint(1, 303); self.station2 = random.randint(1, 303)
		while (self.station1 == self.station2): self.station2 = random.randint(1, 303)

	def WallTime(self):
		A_start = time.time()
		self.itinerary.A_ShortestPath(self.station1, self.station2)
		A_end = time.time() - A_start
		#print(f"A* Algorithm Wall-Time is {A_end} seconds")

		D_start = time.time()
		self.itinerary.D_ShortestPath(self.station1, self.station2)
		D_end = time.time() - D_start
		#print(f"Dijkstra's Algorithm Wall-Time is {D_end} seconds")

		return (A_end, D_end)
	
	def CPUTime(self):
		A_start = time.process_time()
		self.itinerary.A_ShortestPath(self.station1, self.station2)
		A_end = time.process_time() - A_start
		#print(f"A* Algorithm CPU-Time is {A_end} seconds")

		D_start = time.process_time()
		self.itinerary.D_ShortestPath(self.station1, self.station2)
		D_end = time.process_time() - D_start
		#print(f"Dijkstra's Algorithm CPU-Time is {D_end} seconds")

		return (A_end, D_end)

	def test(self, numTests: int):

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
			'Average Wall Time - A* Algorithm': f'{round(A_WallTime * 1000, 5)} ms',
			'Average Wall Time - Dijkstra\'s Algorithm': f'{round(D_WallTime * 1000, 5)} ms',
			'Average CPU Time - A* Algorithm': f'{round(A_CPUTime * 1000, 5)} ms',
			'Average CPU Time - Dijkstra\'s Algorithm': f'{round(D_CPUTime * 1000, 5)} ms',
		}

def main():
	benchmark = Benchmark()
	#benchmark.CPUTime()
	#benchmark.WallTime()
	results = benchmark.test(100)
	for result in results.items():
		print(result)

if __name__ == "__main__":
	main()