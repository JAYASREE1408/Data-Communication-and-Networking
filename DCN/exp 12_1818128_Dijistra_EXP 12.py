# 1818128-BUG SQUASHERS:
# DIJIKSTRA'S ALGORITHM:
import sys   # Import sys module
class Graph(): 

	def __init__(self, vertices): 
		self.V = vertices 
		self.graph = [[int(input()) for x in range (self.V)] for y in range(self.V)] 


	def printSolution(self, dist): 
		print ("The Distance of Each Vertex from the Source: ") 
		for node in range(self.V): 
			print (node, ":", dist[node]) 

	# A utility function to find the vertex with 
	# minimum distance value, from the set of vertices 
	# not yet included in shortest path tree 
	def minDistance(self, dist, sptSet): 

		# Initilaize minimum distance for next node 
		min = sys.maxsize 

		# Search not nearest vertex
		# Shortest path tree 
		for v in range(self.V): 
			if dist[v] < min and sptSet[v] == False: 
				min = dist[v] 
				min_index = v 

		return min_index 

	# Funtion that implements Dijkstra's single source 
	# Shortest path algorithm for a graph represented 
	# Using adjacency matrix representation 
	def dijkstra(self, src): 

		dist = [sys.maxsize] * self.V 
		dist[src] = 0
		sptSet = [False] * self.V 

		for cout in range(self.V): 

			# Pick the minimum distance vertex from 
			# the set of vertices not yet processed. 
			# u is always equal to src in first iteration 
			u = self.minDistance(dist, sptSet) 

			# Put the minimum distance vertex in the 
			# shotest path tree 
			sptSet[u] = True

			# Update dist value of the adjacent vertices 
			# of the picked vertex only if the current 
			# distance is greater than new distance and 
			# the vertex in not in the shotest path tree 
			for v in range(self.V): 
				if self.graph[u][v] > 0 and sptSet[v] == False and dist[v] > dist[u] + self.graph[u][v]: 
					dist[v] = dist[u] + self.graph[u][v] 

		self.printSolution(dist)
# Driver program
g = Graph(int(input("Enter the total no. of vertices: ")))
g.dijkstra(int(input("Enter the Source Node: ")))
