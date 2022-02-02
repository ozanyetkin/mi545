# Ozan Yetkin | 1908227
# Initialize the example input provided
example_input = [51, 18, 54, 52, 60]

# Initialize post from pre function to be implemented
def post_from_pre(preorder):
    # Define the base case which is a BST with zero node, return an empty list
    if len(preorder) == 0:
        return []
    
    # Initialize the root as the first item since it is guaranteed in preorder
    root = preorder[0]
    # Initialize left and right as empty lists
    left = []
    right = []
    # Iterate over each node excluding the root itself
    for node in preorder[1:]:
        # Check if the node in iteration is smaller than the root
        if node < root:
            # If it is the case append the node to left
            left.append(node)
        # Check if the node in iteration is greater than or equal to the root
        else:
            # If it is the case append the node to right
            right.append(node)
    # Call the function on left and right to recursively compute all nodes, return left + right + root for postorder
    return post_from_pre(left) + post_from_pre(right) + [root]

# Test the function with provided example input which should return [18, 52, 60, 54, 51]
print(post_from_pre(example_input))

example_input = [60, 20, 10, 40, 30, 50, 70]

# Test the function with another input from lecture slides just to be sure, which should return [10, 30, 50, 40, 20, 70, 60]
print(post_from_pre(example_input))
