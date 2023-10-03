import heapq
import numpy as np
from VALID_MOVES import valid_moves

def H_score(node, goal, n):
	'''
	Fill in this function to return the heuristic value of the current node.

	Compute heuristic as the Manhattan distance between the 
	current node and the goal state, divided by 
	the largest possible jump value.

	n is the dimensionality of the maze (n x n).

	If using print statements to debug, please make sure 
	to remove them before your final submisison.
	'''
	return heuristic


def ASTAR(maze, start, goal):
	'''
	Fill in this function that uses A* search to find the shortest 
	path using the heuristic function H_score defined above.

	Return the length of the shortest path from the start state 
	to the goal state, and the path itself.

	Your return statement should be of the form:
	return len(path)-1, path

	where path is a list of tuples, corresponding to the 
	path and includes the start state.

	If using print statements to debug, please make sure 
	to remove them before your final submisison.
	'''

