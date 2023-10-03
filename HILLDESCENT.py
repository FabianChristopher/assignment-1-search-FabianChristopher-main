import sys
import numpy as np
from BFS import BFS
from ASTAR import ASTAR


def energyfunction(maze, start, goal):
	'''
	Compute the energy as the sum of the shortest path length 
	from the start state to the goal state (computed using A*)
	and the number of cells that are not reachable from the 
	start state (computed using BFS).

	If using print statements to debug, please make sure
	to remove them before your final submisison.
	'''
	return energy



def HILLDESCENT(maze, start_cell, goal_state, iterations):
	'''
	Fill in this function to implement Hill Descent local search.

	Your function should return the best solution found, 
	which should be a tuple containing 2 elements:

	1. The best maze found, which is a 2-dimensional numpy array.
	2. The energy of the best maze found.

	Note that you should make a local copy of the maze 
	before making any changes to it.

	If using print statements to debug, please make sure
	to remove them before your final submisison.
	'''

	return best_solution



def HILLDESCENT_RANDOM_RESTART(maze, start_cell, goal_state, iterations, num_searches):
	'''
	Fill in this function to implement Hill Descent local search with Random Restarts.

	For a given number of searches (num_searches), run hill descent search.

	Keep track of the best solution through all restarts, and return that.

	Your function should return the best solution found, 
	which should be a tuple containing 2 elements:

	1. The best maze found, which is a 2-dimensional numpy array.
	2. The energy of the best maze found.

	Note that you should make a local copy of the maze 
	before making any changes to it.

	You will also need to keep a separate copy of the original maze
	to use when restarting the algorithm each time.

	If using print statements to debug, please make sure
	to remove them before your final submisison.
	'''

	return best_solution



def HILLDESCENT_RANDOM_UPHILL(maze, start_cell, goal_state, iterations, probability):
	'''
	Fill in this function to implement Hill Descent local search with Random uphill steps.

	At each iteration, with probability specified by the probability
	argument, allow the algorithm to move to a worse state.

	Your function should return the best solution found, 
	which should be a tuple containing 2 elements:

	1. The best maze found, which is a 2-dimensional numpy array.
	2. The energy of the best maze found.

	Note that you should make a local copy of the maze
	before making any changes to it.

	If using print statements to debug, please make sure
	to remove them before your final submisison.
	'''

	return best_solution







