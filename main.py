import time
from random import randrange

filename = 'plecak.txt'
with open(filename, 'r') as file:
    lines = file.readlines()

def transform(line):
    name, values = line.split('=')
    values = values.strip('{} \n')
    return [int(x.strip()) for x in values.split(',')]

length = 30
capacity = 50
random = randrange(15)
start_row = random*4 + 2
print("Dataset: ", random+1)
sizes = transform(lines[start_row])
vals = transform(lines[start_row+1])

tm = time.time()
print("Brute force")
def knapsack_brute_force(cap, n):
    if n == 0 or cap == 0:
        return 0, [0] * len(sizes)

    if sizes[n-1] > cap:
        return knapsack_brute_force(cap, n-1)

    include_value, include_list = knapsack_brute_force(cap - sizes[n-1], n-1)
    include_value += vals[n-1]
    include_list = include_list.copy()
    include_list[n-1] = 1

    exclude_value, exclude_list = knapsack_brute_force(cap, n-1)

    if include_value > exclude_value:
        return include_value, include_list
    else:
        return exclude_value, exclude_list

best_value, best_choice = knapsack_brute_force(capacity, length)
t_weight = 0
for i in range(length):
    if best_choice[i] == 1:
        t_weight += sizes[i]
print("Sizes:", sizes)
print("Values:", vals)
print("Best choice:", best_choice)
print("Total value:", best_value)
print("Total weight:", t_weight)
tm1 = time.time()
print("Time", tm1 - tm)

tm = time.time()
items = [(vals[i] / sizes[i], sizes[i], vals[i], i) for i in range(length)]
sorted_items = sorted(items, key=lambda x: x[0], reverse=True)

temp_wei = 0
temp_val = 0
a = [0]*30
print("Heuristic algorithm")
for value_ratio, weight, value, index in sorted_items:
    if temp_wei + weight <= capacity:
        temp_wei += weight
        temp_val += value
        a[index] = 1

tm2 = time.time()
print("Sizes:", sizes)
print("Values:", vals)
print("Choice", a)
print("Value:", temp_val)
print("Weight:", temp_wei)
print("Execution time):", tm2 - tm1)