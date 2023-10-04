import sys
import numpy as np
from BFS import BFS
from ASTAR import ASTAR
import random

# External Sources used - Python Documentations, Stack OverFlow, Generative AI, YouTube for debugging purposes.

# Returns the energy, taking arguments RJM, start node and goal state.

def energyfunction(maze, start, goal):
    shortest_path_length, _ = ASTAR(maze, start, goal)
    unreachable_cells = np.count_nonzero(BFS(maze, start) == -1)
    energy = shortest_path_length + unreachable_cells
    return energy


# Implements Hill Descent, taking arguments RJM, start state goal state and iterations, returns a tuple containing best maze and best energy.

def HILLDESCENT(maze, start_cell, goal_state, iterations):
    best_maze = maze.copy()
    best_energy = energyfunction(best_maze, start_cell, goal_state)

    for _ in range(iterations):
        x, y = np.random.randint(0, len(maze), size=2)
        if (x, y) != goal_state:
            old_value = maze[x, y]

            while True:
                new_value = random.randint(1, maze.shape[0] - 1)
                if new_value != old_value:
                    break

            maze[x, y] = new_value           
            # maze[x, y] = np.random.randint(1, len(maze))
            new_energy = energyfunction(maze, start_cell, goal_state)
            if new_energy < best_energy:
                best_energy = new_energy
                best_maze = maze.copy()
            else:
                maze[x, y] = old_value

    best_solution = best_maze, best_energy
    return best_solution


# Implements Hill Descent Random Restart, taking arguments RJM, start state, goal state, iterations and num_searches, returns a tuple containing best maze and best energy.

def HILLDESCENT_RANDOM_RESTART(maze, start_cell, goal_state, iterations, num_searches):
    best_maze = None
    best_energy = float('inf')

    for _ in range(num_searches):
        # Make a copy of the maze to work with
        current_maze = maze.copy()

        # Perform hill descent on the current maze
        for _ in range(iterations):
            # Pick a random cell that is not the goal
            while True:
                x, y = np.random.randint(0, len(maze), size=2)
                if (x, y) != goal_state:
                    break

            # Change its jump value to a different random jump value between 1 and k - 1
            old_value = current_maze[x, y]
            # current_maze[x, y] = np.random.randint(1, len(maze))

            while True:
                new_value = random.randint(1, maze.shape[0] - 1)
                if new_value != old_value:
                    break

            maze[x, y] = new_value

            # Compute the new energy
            new_energy = energyfunction(current_maze, start_cell, goal_state)

            # If the new energy is lower, update the best maze and energy
            if new_energy < best_energy:
                best_maze = current_maze.copy()
                best_energy = new_energy
            else:
                # If the new energy is not lower, revert the change
                current_maze[x, y] = old_value

    best_solution = best_maze, best_energy
    
    return best_solution


# Implements Hill Descent Random Uphill, taking arguments RJM, start state, goal state, iterations and probability, returns a tuple containing best maze and best energy.

def HILLDESCENT_RANDOM_UPHILL(maze, start_cell, goal_state, iterations, probability):
    best_maze = maze.copy()
    best_energy = energyfunction(best_maze, start_cell, goal_state)

    for _ in range(iterations):
        # Pick a random cell that is not the goal
        while True:
            x, y = np.random.randint(0, len(maze), size=2)
            if (x, y) != goal_state:
                break

        # Change its jump value to a different random jump value between 1 and k - 1
        old_value = maze[x, y]
        # maze[x, y] = np.random.randint(1, len(maze))

        while True:
                new_value = random.randint(1, maze.shape[0] - 1)
                if new_value != old_value:
                    break

        maze[x, y] = new_value

        # Compute the new energy
        new_energy = energyfunction(maze, start_cell, goal_state)

        # If the new energy is lower, update the best maze and energy
        if new_energy < best_energy:
            best_maze = maze.copy()
            best_energy = new_energy
        else:
            # If the new energy is not lower, revert the change with a certain probability
            if np.random.rand() < probability:
                best_maze = maze.copy()
                best_energy = new_energy
            else:
                maze[x, y] = old_value

    best_solution = best_maze, best_energy

    return best_solution







