## import libraries to test

# built-in list
import numpy as np
import pandas as pd

import quantumrandom
from time import perf_counter_ns
from time import perf_counter

## function definitions to be timed

def performance_test_list_sort(quantum_random_list: "list") -> int:
    
    
    time_start = perf_counter_ns()
    quantum_random_list.sort()
    time_stop = perf_counter_ns()
    
    return time_stop - time_start

def performance_test_ndarray_sort(quantum_random_list: "list") -> int:
    
    quantum_random_list = np.array(quantum_random_list)
    
    time_start = perf_counter_ns()
    quantum_random_list.sort()
    time_stop = perf_counter_ns()
    
    return time_stop - time_start

def performance_test_Series_sort(quantum_random_list: "list") -> int:
    
    quantum_random_list = pd.Series(data=quantum_random_list, dtype='Int64')
    
    time_start = perf_counter_ns()
    quantum_random_list.sort_values()
    time_stop = perf_counter_ns()
    
    return time_stop - time_start
	
## RUN THE EXPERIMENT

## n is the number of arrays that will be created and sorted

n = 100

time_results_l = []
time_results_ndarray = []
time_results_Series = []

print("Starting experiment, this might take a while...")
time_start = perf_counter()
for i in range(n):
    print("...")
    quantum_random_list = quantumrandom.get_data(data_type='uint16', array_length=1000)
    
    time_results_l.append(performance_test_list_sort(quantum_random_list))
    time_results_ndarray.append(performance_test_ndarray_sort(quantum_random_list))
    time_results_Series.append(performance_test_Series_sort(quantum_random_list))
    
time_stop = perf_counter()

print("Experiment ended!, it took", (time_stop-time_start)/60, "minute(s) to finish!" )

results_list = [
    sum(time_results_l)/len(time_results_l),
    sum(time_results_ndarray)/len(time_results_ndarray),
    sum(time_results_Series)/len(time_results_Series)
]

print("Mean time for built-in list: ", sum(time_results_l)/len(time_results_l), "nanosecond(s)")
print("Mean time for Numpy ndarray: ", sum(time_results_ndarray)/len(time_results_ndarray), "nanosecond(s)")
print("Mean time for Pandas Series: ", sum(time_results_Series)/len(time_results_Series), "nanosecond(s)")

with open("test_datastructures_results.txt", "w") as writer:
    writer.write("Mean time for built-in list: " + str(results_list[0]) + "nanosecond(s)\n")
    writer.write("Mean time for Numpy ndarray: " + str(results_list[1]) + "nanosecond(s)\n")
    writer.write("Mean time for Pandas Series: " + str(results_list[2]) + "nanosecond(s)\n")