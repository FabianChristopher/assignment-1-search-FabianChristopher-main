import numpy as np
from VALID_MOVES import valid_moves
from collections import deque


def BFS(maze, start):
    k = len(maze)
    path_lengths = -np.ones((k, k), dtype=int)
    path_lengths[start] = 0

    queue = deque([start])

    while queue:
        cell = queue.popleft()
        for next_cell in valid_moves(maze, cell):
            if path_lengths[next_cell] == -1 or path_lengths[next_cell] > path_lengths[cell] + 1:
                path_lengths[next_cell] = path_lengths[cell] + 1
                queue.append(next_cell)

    path_matrix = path_lengths

    return path_matrix
