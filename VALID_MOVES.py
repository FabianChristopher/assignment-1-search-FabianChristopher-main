def valid_moves(maze, node):
    k = len(maze)
    x, y = node
    steps = maze[node]
    neighbors = []

    # Check all cells horizontally and vertically based on the number of steps.
    if x - steps >= 0:
        neighbors.append((x - steps, y))
    if x + steps < k:
        neighbors.append((x + steps, y))
    if y - steps >= 0:
        neighbors.append((x, y - steps))
    if y + steps < k:
        neighbors.append((x, y + steps))

    return neighbors
