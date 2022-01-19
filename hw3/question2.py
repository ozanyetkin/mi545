# Ozan Yetkin | 1908227
import matplotlib.pyplot as plt
from time import perf_counter

def foo(n):
    if n < 5:
        total = n 
    else:
        total = 0
        for i in [1,2,3]:
            total += foo(n//4 + i)
    while n > 0:
        total += n
        n = n // 2
    return total

n_list = []
t_list = []
for n in range(0, 10000, 100):
    # Start the stopwatch / counter
    t1_start = perf_counter()

    # Call the function with n
    foo(n)

    # Stop the stopwatch / counter
    t1_stop = perf_counter()

    print("Elapsed time:", t1_stop - t1_start)
    n_list.append(n)
    t_list.append(t1_stop - t1_start)

# Plot
fig, ax = plt.subplots()
ax.plot(n_list, t_list, linewidth=2.0)

plt.show()