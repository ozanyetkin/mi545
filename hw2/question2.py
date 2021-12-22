# Ozan Yetkin | 1908227
# Write a recursive function that returns if a given maze is solvable or not

# Initialize a maze that is solvable
maze1 = [
    [0, 1, 1, 1, 0, 0, 0, 1],
    [0, 0, 0, 1, 0, 1, 0, 1],
    [1, 1, 0, 1, 0, 1, 0, 0],
    [1, 1, 0, 1, 0, 0, 1, 0],
    [1, 0, 0, 0, 1, 0, 1, 0],
    [0, 0, 1, 0, 1, 0, 1, 0],
    [0, 1, 1, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 1, 0, 1, 0],
]

# Initialize another maze that is not solvable
maze2 = [
    [0, 1, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 1, 0, 1, 0, 1],
    [1, 1, 0, 1, 0, 1, 0, 0],
    [1, 1, 0, 1, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 1, 1, 1],
    [0, 0, 1, 0, 0, 1, 1, 1],
    [0, 1, 1, 0, 0, 1, 0, 1],
    [0, 0, 0, 0, 1, 1, 0, 0],
]

# Initialize the function that takes maze, start, and goal as input
def is_solvable(maze, start, goal):
    # Initialize the path as a set
    path = set()
    # Use the recursive advance function that returns all valid paths starting from start
    advance(start, maze, path)
    # Check if the goal is inside the valid path, if so return True, if not return False
    if goal in path:
        return True
    else:
        return False

# Define a function that finds neighbors of a given position
def get_neighbors(position, maze):
    # Use all directions [up, right, down, left]
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    # Initialize a neigbors list containing all directions
    neighbors = [(position[0] + dir[0], position[1] + dir[1]) for dir in directions]
    # Filter out the left or right neighbors for elements on edge in y axis
    neighbors = list(filter(lambda p: 0 <= p[0] < len(maze[0]), neighbors))
    # Filter out the up or down neighbors for edge elements in x axis
    neighbors = list(filter(lambda p: 0 <= p[1] < len(maze), neighbors))
    # Return the list containing all the neighbors of an element at specific position
    return neighbors

# Small test for get_neighbors function
# print(get_neighbors((5, 0), maze1))

# Define a function that finds the value at a specific position
def get_value(position, maze):
    # Return the item at index [1][0] not [0][1] since first item is x axis and second is y
    return maze[position[1]][position[0]]

# Small test for both get_value and get_neighbors function
# print([get_value(n, maze1) for n in get_neighbors((5, 0), maze1)])

# Define the advance function that recursively finds valid path starting at a specific position
def advance(position, maze, path):
    # Define the base case to finish recursion when the position is already visited or it is a wall
    if position in path or get_value(position, maze) == 1:
        return
    # If the base case not achieved yet, add the current position to the path set
    path.add(position)
    # Recursively advance using all the neighbors of the current position
    for n in get_neighbors(position, maze):
        advance(n, maze, path)

# Test cases for solvable and not solvable mazes
print(is_solvable(maze1, (0, 0), (7, 7)))
# should print True

print(is_solvable(maze2, (0, 0), (7, 7)))
# should print False

# Just in case, create a bigger maze and test the function
maze3 = [
    [0, 1, 1, 1, 0, 0, 0, 1, 0],
    [0, 0, 0, 1, 0, 1, 0, 1, 0],
    [1, 1, 0, 1, 0, 1, 0, 0, 0],
    [1, 1, 0, 1, 0, 0, 1, 0, 1],
    [1, 0, 0, 0, 1, 0, 1, 0, 1],
    [0, 0, 1, 0, 1, 0, 1, 0, 1],
    [0, 1, 1, 0, 0, 0, 1, 0, 1],
    [0, 0, 0, 0, 1, 0, 1, 0, 0],
    [0, 1, 1, 0, 1, 0, 1, 1, 0],
]

print(is_solvable(maze3, (0, 0), (8, 8)))
