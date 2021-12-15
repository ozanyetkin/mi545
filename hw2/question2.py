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
    pass

# Test cases for solvable and not solvable mazes
print(is_solvable(maze1, (0,0), (7,7)))
# should print True

print(is_solvable(maze2, (0,0), (7,7)))
# should print False