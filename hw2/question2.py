# Ozan Yetkin | 1908227
# Write a recursive function that returns if a given maze is solvable or not

# Initialize a maze that is solvable
maze1 = [[0, 1, 1, 1, 0, 0, 0, 1],
         [0, 0, 0, 1, 0, 1, 0, 1],
         [1, 1, 0, 1, 0, 1, 0, 0],
         [1, 1, 0, 1, 0, 0, 1, 0],
         [1, 0, 0, 0, 1, 0, 1, 0],
         [0, 0, 1, 0, 1, 0, 1, 0],
         [0, 1, 1, 0, 0, 0, 1, 0],
         [0, 0, 0, 0, 1, 0, 1, 0]]

# Initialize another maze that is not solvable
maze2 = [[0, 1, 0, 0, 0, 0, 0, 1],
         [0, 0, 0, 1, 0, 1, 0, 1],
         [1, 1, 0, 1, 0, 1, 0, 0],
         [1, 1, 0, 1, 0, 0, 0, 1],
         [1, 0, 0, 0, 0, 1, 1, 1],
         [0, 0, 1, 0, 0, 1, 1, 1],
         [0, 1, 1, 0, 0, 1, 0, 1],
         [0, 0, 0, 0, 1, 1, 0, 0]]

# Initialize the function that takes maze, start, and goal as input
def is_solvable(maze, start, goal):
    
    path = set()
    advance(start, maze, path)

    if goal in path:
        return True
    else:
        return False


def get_neighbors(position, maze):
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    tmp = [(position[0] + dir[0], position[1] + dir[1]) for dir in directions]
    tmp2 = list(filter( lambda p: 0 <= p[0] < len(maze[0]), tmp))
    neighbors = list(filter( lambda p: 0 <= p[1] < len(maze), tmp2))
    return neighbors

# print(get_neighbors((5, 0), maze1))

def get_value(position, maze):
    return maze[position[1]][position[0]]

def set_value(position, maze):
    maze[position[1]][position[0]] = 1
    return maze

# print([get_value(n, maze1) for n in get_neighbors((5, 0), maze1)])
# print(set_value((0,0), maze1))

def advance(position, maze, path):
    # if get_value(position, maze) == 0 and min([get_value(n, maze) for n in get_neighbors(position, maze)]) == 1:
    if position in path or get_value(position, maze) == 1:
        return
    path.add(position)
    for n in get_neighbors(position, maze):
        # path.add(n)
        advance(n, maze, path)

def get_zeros(maze):
    zeros = []
    for i in range(len(maze)):
        for j in range(len(maze[0])):
            if maze[i][j] == 0:
                zeros.append((j, i))
    return zeros

# print(get_zeros(maze1))
def get_chains(position, path):
    pass

# Test cases for solvable and not solvable mazes
print(is_solvable(maze1, (0,0), (7,7)))
# should print True

print(is_solvable(maze2, (0,0), (7,7)))
# should print False