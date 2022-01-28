# Ozan Yetkin | 1908227
import bisect

example_input = [4, 3, 2, 6]

# First try
def find_min_cost(stick_list):
    cost = 0
    while len(stick_list) > 1:
        stick_list.sort()
        s1 = stick_list.pop(0)
        s2 = stick_list.pop(0)
        cost += s1 + s2
        stick_list.append(s1 + s2)
    return cost

def find_min_cost(stick_list):
    total_cost = 0
    stick_list.sort()
    while len(stick_list) > 1:
        s1 = stick_list.pop(0)
        s2 = stick_list.pop(0)
        cost = s1 + s2
        total_cost += cost
        bisect.insort(stick_list, cost) 
    return total_cost

print(find_min_cost(example_input))

# find_min_cost() Tests

import time
import random

random.seed(42) #For reproducible random tests

test_cases = [([2], 0),
              ([1, 1], 2),
              ([1, 1, 1], 5),
              ([1, 3, 1],  7),
              ([4, 3, 2, 6],  29),
              ([2, 6, 100, 1, 2, 3, 4], 162),
              ([random.randint(1,500) for i in range(1000)], 2440939),
              ([random.randint(1,500) for i in range(2000)], 5382438),
              ([random.randint(1,500) for i in range(5000)], 15234729),
              ([random.randint(1,500) for i in range(10000)], 32602935),
              ([random.randint(1,500) for i in range(20000)], 70341946),
              ([random.randint(1,500) for i in range(50000)], 192366645),
              ([random.randint(1,500) for i in range(100000)], 410104549),]

test_idx = 1
all_tests = True
for tc in test_cases:
    t = time.time()
    if find_min_cost(tc[0]) == tc[1]:
        if time.time() - t > 5.0:
            print("Test %d TOO SLOW!!!" % (test_idx))
            all_tests = False
            break
        else:
            print("Test %d PASSED" % (test_idx))
    else:
        print("Test %d FAILED!!!" % (test_idx))
        all_tests = False
        break
    test_idx += 1
if all_tests:
    print("CONGRATULATIONS! All tests OK!")
else:
    print("You have failing tests! Please try again...")
