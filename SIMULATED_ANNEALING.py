import sys
import numpy as np
from BFS import BFS
from ASTAR import ASTAR
from HILLDESCENT import energyfunction

def SIMULATED_ANNEALING(maze, start_cell, goal_state, iterations, T, decay):

    current_maze = maze.copy()
    current_energy = energyfunction(current_maze, start_cell, goal_state)
    
    best_maze = current_maze.copy()
    best_energy = current_energy

    for _ in range(iterations):
        # Pick a random cell that is not the goal
        while True:
            x, y = np.random.randint(0, len(maze), size=2)
            if (x, y) != goal_state:
                break

        # Change its jump value to a different random jump value between 1 and k - 1
        old_value = current_maze[x, y]
        current_maze[x, y] = np.random.randint(1, len(maze))

        # Compute the new energy
        new_energy = energyfunction(current_maze, start_cell, goal_state)

        # If the new energy is lower, update the current and best mazes and energies
        if new_energy < current_energy:
            current_energy = new_energy
            if new_energy < best_energy:
                best_maze = current_maze.copy()
                best_energy = new_energy
        else:
            # If the new energy is not lower, accept the worse solution with a certain probability
            if np.random.rand() < np.exp((current_energy - new_energy) / T):
                current_energy = new_energy
            else:
                # If the worse solution is not accepted, revert the change
                current_maze[x, y] = old_value
        T *= decay

    best_solution = best_maze, best_energy


    return best_solution
