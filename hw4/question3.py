# Ozan Yetkin | 1908227
# Initialize example input
example_input = [51, 18, 54, 52, 60]

# Initialize post from pre function to be implemented
def post_from_pre(preorder):
    postorder = []
    while len(preorder) > 0:
        current = preorder.pop()
        postorder.append(current)
        if current > postorder[-1]:
            postorder.insert(-1, current)
        else:
            postorder.insert(0, current)
    return postorder

# Test the function which should return [18, 52, 60, 54, 51]
print(post_from_pre(example_input))