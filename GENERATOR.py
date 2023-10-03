import sys
import numpy as np
from BFS import BFS

def generator(k):
    # Create a k * k maze with random integers between 1 and k-1 in each cell.
    init_board = np.random.randint(1, k, size=(k, k))

    # Generate a random start state and a random goal state.
    start_cell = (np.random.randint(0, k), np.random.randint(0, k))
    goal_state = (np.random.randint(0, k), np.random.randint(0, k))

    # Ensure that the start state and the goal state are not the same.
    while start_cell == goal_state:
        goal_state = (np.random.randint(0, k), np.random.randint(0, k))

    # Set the entry in the maze corresponding to the goal state to 0.
    init_board[goal_state] = 0

    return init_board, start_cell, goal_state


def generator_pathcheck(k):
    while True:
        # Generate a random maze, a start state, and a goal state.
        init_board, start_cell, goal_state = generator(k)

        # Use BFS to check if there is a path from the start state to the goal state.
        path_lengths = BFS(init_board, start_cell)

        # If there is a valid path, return the maze, the start state, and the goal state.
        if path_lengths[goal_state] != -1: 
            return init_board, start_cell, goal_state
