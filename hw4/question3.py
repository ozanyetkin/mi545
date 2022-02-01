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

import itertools

def post_from_pre(preorder):
    if not preorder:
        return []
    else:
        root = preorder[0]
        left = list(itertools.takewhile(lambda x: x < root, preorder[1:]))
        right = preorder[len(left) + 1:]
        return post_from_pre(left) + post_from_pre(right) + [root]

# Test the function which should return [18, 52, 60, 54, 51]
print(post_from_pre(example_input))

example_input = [20, 10, 6, 15, 30, 35]

# Test the function which should return [6, 15, 10, 35, 30, 20]
print(post_from_pre(example_input))
