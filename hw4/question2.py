# Ozan Yetkin | 1908227
# Import the built-in bisect and heapq libraries
import bisect
import heapq

# Initialize the example input to test the functions
example_input = [4, 3, 2, 6]

# First try, failing only on the last test
def find_min_cost(stick_list):
    # Initialize the cost as 0
    cost = 0
    # Enter a while loop until at most two sticks left in the stick list
    while len(stick_list) > 1:
        # Sort the sticks using built-in sort method
        stick_list.sort()
        # Pop the two shortest sticks using first index and store them in s1 and s2 variables
        s1 = stick_list.pop(0)
        s2 = stick_list.pop(0)
        # Increment the cost by s1 + s2 which corresponds the new combined stick
        cost += s1 + s2
        # Append the new combined stick to stick list
        stick_list.append(s1 + s2)
    # Return the calculated cost
    return cost

# Second try, passing all the tests but still a bit slow on the last (2.2 seconds)
def find_min_cost(stick_list):
    # Initialize the total cost as 0
    total_cost = 0
    # Sort the stick list once instead of sorting each time inside the loop
    stick_list.sort()
    
    # Enter a while loop until at most two sticks left in the stick list
    while len(stick_list) > 1:
        # Pop the two shortest sticks using first index and store them in s1 and s2 variables
        s1 = stick_list.pop(0)
        s2 = stick_list.pop(0)
        # Calculate cost by adding two shortest sticks together and add it to total cost
        cost = s1 + s2
        total_cost += cost
        # Use built-in bisect module to insert the cost to the correct place in sorted list not to sort each time
        bisect.insort(stick_list, cost)
    # Return the calculated total cost
    return total_cost

# Third try, passing all the tests like charm
def find_min_cost(stick_list):
    # Initialize the total cost as 0 and an empty temporary list to be used as stack for heap sort
    total_cost = 0
    tmp = []

    # Iterate over each stick in the stick list
    for stick in stick_list:
        # Use built-in heappush method to construct a heap queue from sticks
        heapq.heappush(tmp, stick)

    # Sort the sticks before entering the loop using heap sort
    sorted_sticks = [heapq.heappop(tmp) for i in range(len(tmp))]
    
    # Enter a while loop until at most two sticks left in the stick list
    while len(sorted_sticks) > 1:
        # Use built-in heappop module to pop the two shorted sticks
        s1 = heapq.heappop(sorted_sticks)
        s2 = heapq.heappop(sorted_sticks)
        # Calculate cost by adding two shortest sticks together and add it to total cost
        cost = s1 + s2
        total_cost += cost
        # Use built-in heappush module to push the new stick to heap queue
        heapq.heappush(sorted_sticks, cost)
    # Return the calculated total cost
    return total_cost

# Call the function to test if it calculates the total cost given the example input
print(find_min_cost(example_input))

# Run the test harness provided for finding min cost function
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
