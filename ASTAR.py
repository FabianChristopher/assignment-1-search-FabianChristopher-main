import heapq
import numpy as np
from VALID_MOVES import valid_moves
from queue import PriorityQueue


def H_score(node, goal, n):
    # Compute heuristic as the Manhattan distance between the current node and the goal state, divided by the largest possible jump value.
    heuristic = (abs(node[0] - goal[0]) + abs(node[1] - goal[1])) / (n - 1)
    return heuristic


def ASTAR(maze, start, goal):
    k = len(maze)
    path_lengths = {start: 0}
    path_prev = {start: None}
    queue = PriorityQueue()
    queue.put((0, start))

    while not queue.empty():
        _, cell = queue.get()

        if cell == goal:
            break

        for next_cell in valid_moves(maze, cell):
            new_cost = path_lengths[cell] + maze[cell]

            if next_cell not in path_lengths or new_cost < path_lengths[next_cell]:
                path_lengths[next_cell] = new_cost
                priority = new_cost + H_score(next_cell, goal, k)
                queue.put((priority, next_cell))
                path_prev[next_cell] = cell

    path = []
    while cell is not None:
        path.append(cell)
        cell = path_prev[cell]
    path.reverse()

    return len(path) - 1, path

