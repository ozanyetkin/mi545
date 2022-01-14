# Ozan Yetkin | 1908227
import matplotlib.pyplot as plt
from time import perf_counter

# Initialize the algorithms to calculate elapsed time
def question_1a(n):
    k = 0
    for i in range(n):
        k += 1 

def question_1b(n):
    i = 1
    while i < n*n:
        i += 2

def question_1c(n):
    k = 1
    for i in range(n):
        for j in range(i+1,n):
            k += 1

def question_1d(n):
    i = 1
    while i < n*n*n:
        i = i + (2*n)

def question_1e(n):
    i = 1
    while i < n*n:
        i = i + (n // 2)

n_list = []
t_list = []
for n in range(0, 1000, 10):
    # Start the stopwatch / counter
    t1_start = perf_counter()

    # Call the function with n
    question_1e(n)

    # Stop the stopwatch / counter
    t1_stop = perf_counter()

    print("Elapsed time:", t1_stop - t1_start)
    n_list.append(n)
    t_list.append(t1_stop - t1_start)

# plot
fig, ax = plt.subplots()
ax.plot(n_list, t_list, linewidth=2.0)

plt.show()